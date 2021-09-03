<template>
	<uni-popup ref="popup" type="bottom" @change="change">
		<view class="popup-content d-flex flex-column">
			
			<view class="d-flex justify-content-end">
				<image src="/static/images/common/clousex-big.png" class="close_btn" @tap="close"></image>
			</view>
			
			<view class="d-flex flex-fill flex-column justify-content-between">
				<view class="d-flex flex-column">
					<view class="font-size-extra-lg font-weight-bold text-color-base mb-30">欢迎登陆~</view>
					<view class="font-size-base text-color-assist">登录后消费可获取积分，享受更好的服务体验</view>
				</view>
				<view class="d-flex flex-column">
					<button type="primary" class="w-100 font-size-lg mb-30" open-type="getUserInfo" @getuserinfo="getUserInfo">微信一键登陆</button>
					<button type="primary" class="w-100 font-size-lg mb-30" @click="login">账号登录</button>
					<!-- <button type="info" @tap="add">+添加地址</button> -->
					<view class="text-center mb-30 font-size-sm text-color-assist">
						点击登陆剁jiojio，即表示已阅读并同意<font class="text-color-primary">《剁jiojio隐私政策》</font>
					</view>
					<view class="text-center font-primary font-size-sm text-color-primary">《剁jiojio服务指南》</view>
				</view>
			</view>
		</view>
	</uni-popup>
</template>

<script>
	//登录用到了自定义组件弹出框
	import uniPopup from '@/components/uni-popup/uni-popup.vue'
	import { mapMutations } from 'vuex'
	
	export default {
		name: 'LoginPopup',//相当于继承！！！！
		components: {
			uniPopup
		},
		props: {
			
		},
		methods: {
			...mapMutations(['SET_USERINFO', 'SET_ISLOGIN']),
			open() {
				this.$refs['popup'].open()
			},
			close() {
				this.$refs['popup'].close()
			},
			change({show}) {
				this.$emit('change', show)
			},
			getUserInfo(e) {
				//请配置AppID，否则获取失败
				if(e.target.errMsg !== 'getUserInfo:ok') {
					uni.showModal({
						title: '提示',
						content: '您已取消了授权，请重新授权登录',
						showCancel: false
					})
					return
				}
				this.SET_USERINFO(e.target.userInfo)
				this.SET_ISLOGIN(true)
				this.close()
			},
			login() {
				uni.navigateTo({
					url: '/pages/my/login'
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.popup-content {
		background-color: #FFFFFF;
		border-radius: 24rpx 24rpx 0 0;
		height: 50vh;
		padding: 50rpx 40rpx;
	}
	
	.close_btn {
		width: 40rpx;
		height: 40rpx;
	}
</style>
