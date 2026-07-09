<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import request from "../api/request"


const route = useRoute()

const report = ref(null)
const loading = ref(true)
const error = ref("")

async function download(type){

  try{

    const response = await request.get(
      `/api/reports/${route.params.id}/export/${type}`,
      {
        responseType:"blob"
      }
    )


    const blob = new Blob(
      [response.data]
    )


    const url = window.URL.createObjectURL(blob)


    const a = document.createElement("a")

    a.href = url

    a.download =
      type === "pdf"
      ? "report.pdf"
      : "report.docx"


    a.click()


    window.URL.revokeObjectURL(url)


  }catch(e){

    alert(
      "下载失败"
    )

  }

}

async function loadReport(){

  try{

    const res = await request.get(
      `/api/reports/${route.params.id}`
    )

    report.value = res.data


  }catch(e){

    error.value =
      e.response?.data?.detail ||
      "加载失败"

  }
  finally{

    loading.value=false

  }

}


onMounted(()=>{
  loadReport()
})


</script>


<template>

<div class="detail">


<p v-if="loading">
加载中...
</p>


<p v-if="error">
{{error}}
</p>


<div v-if="report">


<h1>
{{report.filename}}
</h1>

<div class="actions">

<button
@click="download('pdf')"
>
下载 PDF
</button>


<button
@click="download('docx')"
>
下载 DOCX
</button>

</div>

<p>
生成时间：
{{report.created_at}}
</p>


<hr>


<h2>
摘要
</h2>

<p>
{{report.summary}}
</p>


<h2>
关键点
</h2>

<ul>

<li
v-for="item in report.key_points"
:key="item"
>
{{item}}
</li>

</ul>


<h2>
风险
</h2>

<ul>

<li
v-for="item in report.risks"
:key="item"
>
{{item}}
</li>

</ul>


<h2>
建议
</h2>

<ul>

<li
v-for="item in report.suggestions"
:key="item"
>
{{item}}
</li>

</ul>


</div>


</div>

</template>