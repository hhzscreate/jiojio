<template>
	<view class="container">
		<image class="w-100" mode="widthFix"></image>
		<view class="content">
			<view class="welcome" @tap="openLoginPopup">
				<!-- 有点问题：显示不出名字 -->
				<view>你好 {{ isLogin ? userName : "立即登录" }}</view>
				<view class="font-size-base">美味尽享，认真制作</view>
			</view>
			<!-- member card begin -->
			<view class="member-card">
				<view class="info">
					<view class="title">
						<view class="wenyue-font" @tap="openBenefits">会员</view>
						<view class="tips" @tap="openMember">
							<view>成为会员享双倍积分</view>
							<image src="/static/images/my/icon_arrow.png"></image>
						</view>
					</view>
					<image @tap="info" src="https://wx.qlogo.cn/mmopen/vi_32/Hx7MFkCEmZVHziaTTiaHSiaCs4ApnH5CD0nYOhOg1nYUUMYtxMXkL6L4VL5icRfO5w4LGzW5ib0FZicwj2MficyYfZgCw/132" class="avatar"></image>
					<view class="badage">
						Lv1
					</view>
				</view>
				<view class="row">
					<navigator class="grid" open-type="navigate" url="/pages/integrals/mall">
						<image src="/static/images/my/me_icon_points.png"></image>
						<view class="value">63</view>
						<view class="title">积分商城</view>
					</navigator>
					<view class="grid" hover-class="opacity-6">
						<image src="/static/images/my/me_icon_quan.png"></image>
						<view class="value">0</view>
						<view class="title">喜茶劵</view>
					</view>
					<navigator class="grid" open-type="navigate" url="/pages/my/wallet">
						<image src="/static/images/my/me_icon_wallet.png"></image>
						<view class="value">0.00</view>
						<view class="title">钱包</view>
					</navigator>
					<navigator class="grid" open-type="navigate" url="/pages/gifts/gifts">
						<image src="/static/images/my/me_icon_gift_card.png"></image>
						<view class="value">0</view>
						<view class="title">阿喜有礼</view>
					</navigator>
				</view>
			</view>
			<!-- member card end -->
		</view>

		

		<list-cell hover arrow>
			<view class="list-cell-wrapper">
				<view view="title">兑换中心</view>
				<view class="subtitle">兑换各种惊喜礼品！</view>
			</view>
		</list-cell>

		<list-cell hover arrow>
			<view class="list-cell-wrapper">
				<view view="title">联系客服</view>
			</view>
		</list-cell>
		<list-cell hover arrow>
			<view class="list-cell-wrapper">
				<view view="title">消息中心</view>
			</view>
		</list-cell>
		<list-cell hover arrow last>
			<view class="list-cell-wrapper">
				<view view="title">更多</view>
			</view>
		</list-cell>
		<!-- 登录popup -->
		<login-popup ref="loginPopup"></login-popup>
	</view>
</template>

<script>
	import listCell from '@/components/list-cell/list-cell.vue'
	import loginPopup from './components/login-popup.vue'
	import { mapState } from 'vuex'
	
	export default {
		components: {
			listCell,
			loginPopup
		},
		data() {
			// return {
			// 	boardcast: [],
			// 	item:"http://127.0.0.1:8000/upload/10.jpg",
			// 	isLogin:false,
			// 	openId:"",
			// 	userName:""
			// }
		},
		// computed: {
		// 	//mapState通过扩展运算符将store.state.orderList 映射this.orderList
		// 	//意思是把store里面的isLogin取出来了，变成了this.isLogin!!
		// 	//即取出了两个数据isLogin和userInfo，可以通过this进行调用
			
		// 	//那么可以把这些定义成全局变量
		// 	...mapState(['isLogin', 'userInfo'])
		// },
		//globaldata要在onload或者onshow上面赋值
		onLoad() {
			//this.boardcast = await this.$api('boardcast')
			this.isLogin=getApp().globalData.isLogin
			this.openId=getApp().globalData.openId
			this.userName=getApp().globalData.userName
			
			
		},
		onShow(){
			//this.closeLoginPopup()  
			//有点问题，会报错说未定义
			
			//onshow才会刷新
			this.isLogin=getApp().globalData.isLogin
			this.openId=getApp().globalData.openId	
			this.userName=getApp().globalData.userName
			
			//console.log(this.openId)
		},
		methods: {
			openLoginPopup() {
				if(this.isLogin) {
					return
				}
				////继承的获取dom方法,即本页面中loginPopup组件执行继承的父亲方法
				this.$refs['loginPopup'].open()
			},
			closeLoginPopup(){
				this.$refs['loginPopup'].close()//回来就关闭
			},
			info() {
				if(this.isLogin){
					uni.navigateTo({
						// url: '/pages/addresses/set?id=' + id
						url: '/pages/my/info?user_id='+this.openId
					}	)
				}
				else{
					uni.showModal({
					    title: '登录提示',
					    content: '您还未登录，是否登录？',
					    success(res) {
					      if (res.confirm) {
					        uni.switchTab({
					        	url:"/pages/my/my"
					        })
					      }
					    }
					  });
				}
				
			},
			taskCenter() {
				uni.navigateTo({
					url: '/pages/task-center/task-center'
				})
			},
			openMember() {
				uni.navigateTo({
					url: '/pages/my/member'
				})
			},
			myCode() {
				uni.navigateTo({
					url: '/pages/my/code'
				})
			},
			openBenefits() {
				if(this.isLogin) {
					uni.navigateTo({
						url: '/pages/my/benefits'
					})
				} else {
					this.$refs['loginPopup'].open()
				}
			}
		}
	}
</script>

<style lang="scss" scoped>
/* #ifdef H5 */
page {
	height: auto;
	min-height: 100%;
}
/* #endif */

.content {
	padding: 0 30rpx;
}

.welcome {
	position: relative;
	margin-top: -136rpx;   //这样子就嵌入图片中了
	display: flex;
	flex-direction: column;
	font-size: $font-size-lg;
	color: $text-color-warning;
}

.member-card {
	background-color: $bg-color-white;
	padding: 20rpx;
	display: flex;
	flex-direction: column;
	border-radius: $border-radius-base;
	margin-bottom: 40rpx;
	
	.info {
		position: relative;
		margin-top: -50rpx;
		display: flex;
		align-items: center;
		position: relative;
		padding: 20rpx 0;
		border-bottom: 1rpx solid rgba($color: $border-color, $alpha: 0.3);
		
		.title {
			flex: 1;
			font-size: 40rpx;
			color: $text-color-base;
			display: flex;
			align-items: center;
		
			.tips {
				margin-left: 10rpx;
				font-size: $font-size-sm;
				color: $text-color-assist;
				background-color: #e9e9e9;
				padding: 10rpx 30rpx;
				border-radius: 50rem !important;
				display: flex;
				align-items: center;
				
				image {
					width: 20rpx;
					height: 20rpx;
				}
			}
		}
		
		.avatar {
			width: 150rpx;
			height: 150rpx;
			border-radius: 100%;
		}
		
		.badage {
			font-family: 'neutra';
			position: absolute;
			bottom: 20rpx;
			left: 0;
			border: 2rpx solid $text-color-base;
			padding: 2rpx 20rpx;
			border-radius: $border-radius-lg;
			font-size: $font-size-base;
		}
	}
	
	.row {
		margin-top: $spacing-row-base;
		width: 100%;
		display: flex;
		align-items: center;

		.grid {
			flex: 1;
			flex-shrink: 0;
			display: flex;
			flex-direction: column;
			align-items: center;
			
			image {
				width: 100rpx;
				height: 100rpx;
			}
			
			.value {
				font-family: 'neutra';
				margin-bottom: $spacing-col-sm;
				font-size: $font-size-lg;
			}
			
			.title {
				font-size: $font-size-sm;
				color: $text-color-grey;
			}
		}
	}
}

.xinqiubobao {
	width: 100%;
	position: relative;
	
	.title {
		margin: 10rpx 0;
		font-size: $font-size-lg;
		font-weight: 500;
	}
	
	.swiper {
		height: 200rpx;
		margin-bottom: 10rpx;
		
		.swiper-item {
			
			.swiper-item-wrapper {
				display: flex;
				background-color: $bg-color-white;
				padding: 40rpx 60rpx;
				border-radius: $border-radius-base;
				align-items: center;
				margin-right: 40rpx;
				
				image {
					width: 100rpx;
					height: 100rpx;
					border-radius: 100%;
					margin-right: 20rpx;
				}
				
				.desc {
					display: flex;
					flex-direction: column;
					
					.title {
						font-size: $font-size-medium;
						font-weight: 500;
						margin-bottom: 10rpx;
					}
					
					.desc {
						font-size: $font-size-sm;
						color: $text-color-grey;
					}
				}
			}
		}
	}
}

.task-center {
	margin: 40rpx 0;
	background-color: $bg-color-white;
	padding: 10rpx 0;
	display: flex;
	align-items: center;
	border-radius: $border-radius-lg;
	
	.intro {
		flex: 1;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		.title {
			font-size: $font-size-lg;
			color: $text-color-base;
		}
		.subtitle {
			font-family: 'neutra';
			font-size: $font-size-sm;
		}
	}
	
	.image-wrapper {
		flex: 1;
		display: flex;
		justify-content: center;
		align-items: center;
		
		image {
			width: 200rpx;
			height: 200rpx;
		}
	}
}

.open-gift {
	width: 100%;
	background-color: $bg-color-white;
	padding: 30rpx 40rpx;
	margin-bottom: 20rpx;
	
	.header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: 20rpx;
		
		.title {
			font-size: $font-size-lg;
			font-weight: 500;
		}
		
		.subtitle {
			font-size: $font-size-base;
			color: $text-color-grey;
		}
	}
	
	.row {
		display: flex;
		flex-wrap: wrap;
		
		.grid {
			width: 33.3333%;
			display: flex;
			flex-direction: column;
			align-items: center;
			padding: 20rpx;
			
			image {
				width: 70rpx;
				height: 70rpx;
				margin-bottom: $spacing-row-base;
			}
			
			.title {
				font-size: $font-size-base;
				color: $text-color-base;
				display: flex;
				align-items: baseline;
				
				.number {
					margin-left: 5rpx;
					font-family: 'neutra';
					color: $color-warning;
				}
			}
		}
	}
}

.list-cell-wrapper {
	width: 100%;
	display: flex;
	justify-content: space-between;
	align-items: center;
	
	.title {
		font-size: $font-size-lg;
	}
	
	.subtitle {
		font-size: $font-size-sm;
		color: $text-color-assist;
	}
}
</style>
