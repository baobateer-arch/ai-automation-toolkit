<script setup>
import { ref, onMounted } from "vue"
import request from "../api/request"
import UploadBox from "../components/UploadBox.vue"


const reports = ref([])
const loading = ref(false)
const error = ref("")


async function loadReports(){

  loading.value = true

  try{

    const res = await request.get(
      "/api/reports"
    )

    reports.value = res.data

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
  loadReports()
})


</script>


<template>

<div class="dashboard">


<h1>
AI 文档分析 Dashboard
</h1>

<UploadBox @uploaded="loadReports" />

<p v-if="loading">
加载中...
</p>


<p v-if="error">
{{error}}
</p>


<section>

<h2>
我的报告
</h2>


<div
v-if="reports.length===0"
>
暂无报告
</div>


<div
v-for="r in reports"
:key="r.id"
class="report-card"
@click="$router.push(`/report/${r.id}`)"
>


<h3>
{{r.filename}}
</h3>


<p>
{{r.summary}}
</p>


<p>
{{r.created_at}}
</p>


</div>


</section>


</div>

</template>