<script setup>
import { ref } from "vue"
import request from "../api/request"

const file = ref(null)
const loading = ref(false)
const message = ref("")

const emit = defineEmits([
  "uploaded"
])


function chooseFile(e){
  file.value = e.target.files[0]
}


async function upload(){

  if(!file.value){
    message.value = "请选择PDF文件"
    return
  }


  const formData = new FormData()

  formData.append(
    "file",
    file.value
  )


  loading.value = true
  message.value = ""


  try{

    await request.post(
      "/api/analyze-pdf",
      formData,
      {
        headers:{
          "Content-Type":"multipart/form-data"
        }
      }
    )


    message.value="分析完成"

    emit("uploaded")


  }catch(e){

    message.value =
      e.response?.data?.detail ||
      "上传失败"

  }
  finally{

    loading.value=false

  }

}

</script>


<template>

<div class="upload-box">

<h2>
上传PDF分析
</h2>


<input
type="file"
accept=".pdf"
@change="chooseFile"
/>


<button
@click="upload"
:disabled="loading"
>

{{loading ? "分析中..." : "开始分析"}}

</button>


<p>
{{message}}
</p>


</div>

</template>