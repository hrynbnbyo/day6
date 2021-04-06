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
                        <a href="#">Main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    update Emp info:
                </h1>
                <form action="emplist.html" method="post">
                    <table cellpadding="0" cellspacing="0" border="0"
                           class="form_table">
                        <tr>
                            <td valign="middle" align="right">
                                name:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="name" v-model="name"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                photo:
                            </td>
                            <td valign="middle" align="left">
                                <input type="file" name="photo" ref="photo"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                salary:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="salary" v-model="salary"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                age:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="age" v-model="age"/>
                            </td>
                        </tr>
                        <tr>
                        <td valign="middle" align="right">部门:</td>
                        <td valign="middle" align="left">
                            <select name="dept" id="" v-model="dept">
                                    <option v-for="(dept,i) in deptlist":key="i" :value="dept.id">{{ dept.dept_name }}</option>
                            </select>
                        </td>
                    </tr>
                    </table>
                    <p>
                        <input type="submit" class="button" value="Confirm" @click="update_emp"/>
                    </p>
                </form>
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
        name: "Update",
        data(){
            return{
                name:"",
                salary:"",
                age:"",
                deptlist:[],
            }
        },
        methods:{
            get_dept_list(){
                this.$axios({
                    url: "http://127.0.0.1:8000/emp/dept/",
                    method: "get",
                }).then(res => {
                    this.deptlist = res.data
                }).catch(error => {
                    console.log(error);
                })
            },
            update_emp() {
                let emp_id = this.$route.params.id
                // ajax上传文件请求要求：enctype必须是 multipart/formData  必须是post请求
                // ajax上传文件必须借助于formData对象
                let formData = new FormData();
                // 将所有的属性添加至formData中 参数1：后台接受的key  参数2：用户输入的值
                formData.append("emp_name", this.name)
                formData.append("age", this.age)
                formData.append("photo",this.$refs.photo.files[0])
                formData.append("salary", this.salary)
                formData.append("dept",this.dept)
                this.$axios({
                    url: "http://127.0.0.1:8000/emp/employees/"+emp_id+"/",
                    method: 'patch',
                    data: formData,     // 将formData作为参数传递过去
                    // 指定请求头相关参数
                    headers: {
                        // 当前请求时包含文件
                        'content-type': "multipart/form-data"
                },
                }).then(res => {
                    console.log(res.data);
                    this.$message.success("员工修改成功");
                    // 添加成功后跳转至列表页
                    this.$router.push("/index");
                }).catch(error => {
                    console.log(error);
                    this.$message.error("失败");
                })
            },
        },
        created() {
            let id = sessionStorage.id;
            if (id) {
                this.$message.success("正在跳转");
            } else {
                this.$message.error("对不起，您还未登录，请登录后在访问");
                this.$router.push("/login");
            }
            let emp_id = this.$route.params.id
            this.$axios({
                url: "http://127.0.0.1:8000/emp/employees/"+emp_id+"/",
                method: 'get'
            }).then(res=>{
                console.log(res.data)
                this.name = res.data.emp_name
                this.photo = res.data.photo
                this.age = res.data.age
                this.salary = res.data.salary
                console.log(res.data)
            }).catch(error=>{
                console.log(error);
            })
            // 调用获取员工列表数据的方法
            this.get_dept_list()

        },
    }
</script>

<style scoped>

</style>
