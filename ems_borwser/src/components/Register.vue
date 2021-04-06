<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    注册
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            用户名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="username" v-model="name" @blur="username"/>
                            <span id="name_msg" style="color: red"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            真实姓名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="real_name" @blur="realname"/>
                            <span id="realname_msg" style="color: red"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="password" @blur="pwd"/>
                            <span id="pwd_msg" style="color: red"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            确认密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="re_pwd" v-model="re_pwd" @blur="repwd"/>
                            <span id="repwd_msg" color="red"style="color: red"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            性别:
                        </td>
                        <td valign="middle" align="left">
                            男
                            <input @click="gender=0" type="radio" class="inputgri" name="sex" value="m"
                                   checked="checked"/>
                            女
                            <input @click="gender=1" type="radio" class="inputgri" name="sex" value="f"/>
                        </td>
                    </tr>

                </table>
                <p>
                    <input type="submit" class="button" value="注册" @click="user_register"/>
                    <router-link to="/login">登录</router-link>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                name: "",
                real_name: "",
                password: "",
                re_pwd: "",
                gender: 0,
            }
        },
        methods: {
            username:function() {
                let username = this.name;
                if (username === null || username === "") {
                    document.getElementById("name_msg").innerHTML = "用户名不能为空";
                } else {
                    document.getElementById("name_msg").innerHTML = "";
                }
            },
            realname:function() {
                let realname = this.real_name;
                if (realname === null || realname === "") {
                    document.getElementById("realname_msg").innerHTML = "姓名不能为空";
                } else {
                    document.getElementById("realname_msg").innerHTML = "";
                }
            },
            pwd:function() {
                let user_pwd = this.password;
                let pattern = /^[a-zA-Z][a-zA-Z0-9\_\.\@\!\#\$\%\^\&\*\(\)]{5,16}/;
                if (user_pwd === null || user_pwd === "") {
                    document.getElementById("pwd_msg").innerHTML = "密码不能为空";
                } else if (pattern.test(user_pwd) === false) {
                    document.getElementById("pwd_msg").innerHTML = "密码强度太低";
                    // 代表校验通过
                } else {
                    document.getElementById("pwd_msg").innerHTML = "";
                }
            },
            repwd:function() {
                let re_pwd = this.re_pwd;
                let user_pwd = this.password;
                if (re_pwd === user_pwd) {
                    document.getElementById("repwd_msg").innerHTML = "";
                } else {
                    document.getElementById("repwd_msg").innerHTML = "两次输入不一致";
                }
            },
            user_register() {
                // 向后端发送请求进行用户注册
                this.$axios({
                    url: "http://127.0.0.1:8000/api/users/",
                    method: "post",
                    data: {
                        name: this.name,
                        real_name: this.real_name,
                        password: this.password,
                        re_pwd: this.re_pwd,
                        gender: this.gender,
                    }
                }).then(res => {
                    console.log(res.data);
                    this.$message({
                        message: "恭喜您注册成功",
                        type: "success",
                        duration: 1000,
                        showClose: true
                    })

                    // 如果注册成功，则自动跳转到登录页
                    this.$router.push("/login");

                }).catch(error => {
                    console.log(error);
                    this.$message.error("您提交的信息有误，请修改后提交~")
                })
            },
        }
    }
</script>

<style scoped>

</style>
