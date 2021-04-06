    <template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                        <a href="javascript:;" @click="user_logout">安全退出</a>
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
                <h1>{{admin_name}},欢迎您访问百知教育管理系统!!</h1>
                <table class="table">
                    <tr class="table_header">
                        <td>ID</td>
                        <td>Name</td>
                        <td>Photo</td>
                        <td>Salary</td>
                        <td>Age</td>
                        <td>Department</td>
                        <td>Operation</td>
                    </tr>
                    <tr class="row1" v-for="(emp,i) in emplist":key="i">
                        <td>{{emp.id}}</td>
                        <td>{{emp.emp_name}}</td>
                        <td><img style="height: 60px;" :src="emp.photo"></td>
                        <td>{{emp.salary}}</td>
                        <td>{{emp.age}}</td>
                        <td>{{emp.dept_name}}</td>
                        <td><a href="javascript:;" @click="del(emp.id)" >delete emp</a>&nbsp;| <a href="javascript:;" @click="update(emp.id)">update emp</a></td>
                    </tr>

                </table>
                <p>
                    <el-button>
                        <router-link to="/add">添加员工</router-link>
                    </el-button>
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
        name: "Index",
        data() {
            return {
                admin_name: '',
                emplist:[],
                id:'',
            }
        },
        methods: {
            del(i) {
                this.$axios({
                    url: "http://127.0.0.1:8000/api/users/",
                    method: "delete",
                    params:{
                        id:i,
                    }
                }).then(res => {
                      this.$message.success("删除成功")
                }).catch(error=>{
                    console.log(error)
                    this.$message.error("删除失败")
                })
            },
            update(i){
                this.$router.push("/update/"+i)
            },
            user_logout() {
                sessionStorage.removeItem("id")
                sessionStorage.removeItem("name")
                // 删除成功则跳转到首页
                this.$router.push("/login")
            },
            // 获取员工列表数据
            get_emp_list() {
                this.$axios({
                    url: "http://127.0.0.1:8000/emp/employees/",
                    method: "get",
                }).then(res => {
                    this.emplist = res.data
                }).catch(error => {
                    console.log(error);
                })
            },
         },
        // 在加载组件前判断用户是否登录，登录可以访问，未登录不能访问
        created() {
            let id = sessionStorage.id;
            if (id) {
                this.admin_name = sessionStorage.name;
            } else {
                this.$message.error("对不起，您还未登录，请登录后在访问");
                this.$router.push("/login");
            }

            // 调用获取员工列表数据的方法
            this.get_emp_list()

        },
    }
</script>

<style scoped>

</style>
