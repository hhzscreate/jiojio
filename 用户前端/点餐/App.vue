<script>
	export default {
		onLaunch: function() {
		},
		onShow: function() {
		},
		onHide: function() {
		},
		globalData:{
			isLogin:false,//#是否登录
			openId:'',//账号id
			userName:'',
			userId:'',//用户信息
			address:{},
			orderType:'takein'
		},
	}
</script>

<!-- 载入全局样式 -->
<style lang="scss">
	@import '~@/static/styles/app.scss';
</style>
