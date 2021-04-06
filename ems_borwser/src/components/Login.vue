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
                <h1>login</h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            username:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" v-model="name" @blur="username"/>
                            <span id="name_msg" style="color: red"></span>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            password:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" v-model="password" @blur="pwd"/>
                            <span id="pwd_msg" style="color: red"></span>
                        </td>
                    </tr>
                </table>
                <p>
                    <input type="submit" class="button" value="登录" @click="user_login"/>
                    &nbsp;&nbsp;
                    <router-link to="/register">注册</router-link>
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
        name: "Login",
        data() {
            return {
                name: "",
                password: "",
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
            pwd:function() {
                let pwd = this.password;
                if (pwd === null || pwd === "") {
                    document.getElementById("pwd_msg").innerHTML = "密码不能为空";
                } else {
                    document.getElementById("pwd_msg").innerHTML = "";
                }
            },

            user_login() {
                this.$axios({
                    url: "http://127.0.0.1:8000/api/users/",
                    method: "get",
                    params: {
                        name: this.name,
                        password: this.password
                    }
                }).then(res => {
                    console.log(res.data.results['id']);
                    if (res.data.message) {
                        this.$message.success("恭喜你，登录成功")
                        // 将用户的信息保存至 sessionStorage  用于展示用户信息
                        sessionStorage.id = res.data.results["id"];
                        sessionStorage.name = res.data.results["name"];
                        // 登录成功则跳转到首页
                        this.$router.push("/index")
                    } else {
                        this.$message.error("您的登录信息有误")
                    }
                }).catch(error => {
                    console.log(error);
                    this.$message.error("您的登录信息有误")
                })
            },
        }
    }
</script>

<style scoped>

</style>
