<template>
  <el-container style="height: 100%;">
    <div id="loginBgCanvas">
      <div class="login-center-bg">
        <div class="login-logo"><img src="../assets/img/login_logo.png" alt=""></div>
        <div class="login-form-box">
          <div class="login-form-title">Welcome to <span style="margin-left: 10px; font-size: 28px;font-weight: bold;">HSTL</span></div>
          <div class="login-form">
            <el-form ref="ruleForm" :model="loginForm" :rules="rules" style="width: 100%;">
              <el-form-item prop="WorkNumber">
                <el-input placeholder="请输入工号" v-model="loginForm.WorkNumber" @keyup.enter.native="submitForm('ruleForm')">
                  <i slot="prefix" class="el-input__icon el-icon-s-custom"></i>
                </el-input>
              </el-form-item>
              <el-form-item prop="password">
                <el-input placeholder="请输入密码" v-model="loginForm.password" show-password @keyup.enter.native="submitForm('ruleForm')">
                  <i slot="prefix" class="el-input__icon el-icon-lock"></i>
                </el-input>
              </el-form-item>
              <el-form-item>
                <el-checkbox v-model="loginForm.rememb" class="remembCheckbox">记住密码</el-checkbox>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" :loading="isSubLoadding" @click="submitForm('ruleForm')" style="width: 100%;">登录</el-button>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </div>
    </div>
  </el-container>
</template>

<script>
  export default {
    name: "login",
    data(){
      return{
        color:"#082F4C",
        loginForm:{
          WorkNumber:"",
          password:"",
          rememb:false
        },
        rules:{
          WorkNumber:[
            {required: true, message: '请输入工号', trigger: 'blur'}
          ],
          password:[
            {required: true, message: '请输入密码', trigger: 'blur'}
          ]
        },
        isSubLoadding:false,
      }
    },
    created(){

    },
    mounted(){
      this.getCookie()
    },
    methods:{
      submitForm(formName){
        let params = {
          WorkNumber:this.loginForm.WorkNumber,
          password:this.loginForm.password
        };
        this.$refs[formName].validate((valid) => {
          if (valid) {
            if(this.isSubLoadding == false){
              this.isSubLoadding = true
              this.axios.post('/api/account/userloginauthentication',this.qs.stringify(params)).then(res =>{
                if(res.data == "OK"){
                  this.$message({
                    showClose: true,
                    message: "登录成功",
                    type: 'success'
                  });
                  var that = this;
                  this.isSubLoadding = false
                  setTimeout(function(){
                    that.$router.push("/Index")
                  },1000)
                  this.$store.commit('setUser',this.loginForm.WorkNumber);
                  if(this.loginForm.rememb){
                    this.setCookie(this.loginForm.WorkNumber,this.loginForm.password,this.loginForm.rememb,7)
                  }else{
                    this.clearCookie()
                  }
                }else{
                  this.$message({
                    showClose: true,
                    type: 'info',
                    message: res.data
                  });
                  this.isSubLoadding = false
                }
              },res =>{
                console.log("请求错误")
                this.isSubLoadding = false
              })
            }
          }
        })
      },
      setCookie(c_name, c_pwd,c_rememb, exdays) {
        var exdate = new Date(); //获取时间
        exdate.setTime(exdate.getTime() + 24 * 60 * 60 * 1000 * exdays); //保存的天数
        //字符串拼接cookie
        window.document.cookie = "userName" + "=" + c_name + ";path=/;expires=" + exdate.toGMTString();
        window.document.cookie = "userPwd" + "=" + c_pwd + ";path=/;expires=" + exdate.toGMTString();
        window.document.cookie = "rememb" + "=" + c_rememb + ";path=/;expires=" + exdate.toGMTString();
      },
      getCookie:function () {
        if (document.cookie.length>0) {
          var arr=document.cookie.split('; ');//这里显示的格式需要切割一下自己可输出看下
          for(var i=0;i<arr.length;i++){
            var arr2=arr[i].split('=');//再次切割
            //判断查找相对应的值
            if(arr2[0]=='userName'){
              this.loginForm.WorkNumber=arr2[1];//保存到保存数据的地方
            }else if(arr2[0]=='userPwd'){
              this.loginForm.password=arr2[1];
            }else if(arr2[0]=='rememb'){
              this.loginForm.rememb=Boolean(arr2[1]);
            }
          }
        }
      },
      clearCookie:function () {
        this.setCookie("","","",-1);
      },
    }
  }
</script>

<style scoped>
  #loginBgCanvas{
    height: 100%;
    width: 100%;
    background: url("../assets/img/login_bg.png") no-repeat center fixed;
  }
  .login-center-bg{
    width: 1100px;
    margin: 15% auto;
  }
  .login-logo{
    width: 40%;
    display: inline-block;
    float: left;
  }
  .login-logo img{
    width: 500px;
    margin: 0 auto;
  }
  .login-form-box{
    width: 400px;
    padding: 20px;
    background: #fff;
    display: inline-block;
    height: 400px;
    float: right;
    margin: 25px;
    border-radius: 3px;
    box-shadow: 0px 0px 5px #fff;
  }
  .login-form{
    width: 100%;
    height: 100%;
    padding: 40px;
    display: flex;
    align-items: center;
  }
  .login-form-title{
    position: relative;
    top: 20px;
    height: 40px;
    line-height: 40px;
    color: #0080c7;
    font-size: 24px;
    display: table;
    padding: 0 40px;
    border-radius:8px;
    margin: 0 auto;
    z-index: 1;
  }
</style>
