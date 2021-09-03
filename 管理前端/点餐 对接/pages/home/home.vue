<!--这个是首页的设计-->
<template>
	<view class="container">
		
		<!-- section-1 begin    这部分设计的是轮播图 -->
		<!-- swiper是滑块视图容器，可以用于轮播图 -->
		<!-- class是指明他的种类，以方便在style中设定相应的样式 -->
		<!-- circular:是否采用衔接滑动，即播放到末尾后重新回到开头
		internal:自动切换时间间隔
		duration:滑动动画时长 -->
		
		<swiper class="banner-swiper"  circular autoplay :interval="5000" :duration="1000">
			<!-- 每一个轮播项是一个swiper-item -->
			<swiper-item class="banner-swiper-item"   v-for="(item, index) in swipers" :key="index">
				<image :src="item.img" mode="widthFix"></image>
			</swiper-item>
		</swiper>
		
		<view class="content">	
			<!-- section-1 begin    这部分设计的是菜单预览和菜单上新 -->
			<view class="section-1">
				<!-- url="/pages/index/index" 原本指向url-->
				<navigator class="item" open-type="switchTab" url="../mart/mart"  hover-class="none">
					<!-- <image src="/static/images/home/home_icon_ziqu1.png" mode="widthFix"></image> -->
					<view class="wenyue-font">菜单管理</view>
					<view class="text-color-assist">对店铺的菜进行管理</view>
				</navigator>
				<navigator class="item" open-type="navigate" url="/pages/addresses/add" hover-class="none">
					<!-- <image src="/static/images/home/home_icon_waimai1.png" mode="widthFix"></image> -->
					<view class="wenyue-font">菜单上新</view>
					<view class="text-color-assist">增加新的菜</view>
				</navigator>
			</view>
			<!-- section-1 end -->
			
			
			
			
			
			<!-- section-2 begin -->
			<view class="section-2">
				
				<navigator class="item"  open-type="switchTab"  url="/pages/preorder/preorder" hover-class="none">
					<view class="title">
						<!-- <image src="/static/images/home/home_icon_baihuo1.png"></image> -->
						<view>订单管理</view>
					</view>
					<view class="tips"> 接单完成订单</view>
				</navigator>
				<navigator class="item" open-type="switchTab" url="/pages/my/my" hover-class="none">
					<view class="title">
						<!-- <image src="/static/images/home/home_icon_qiye1.png"></image> -->
						<view>用户信息管理</view>
					</view>
					<view class="tips">删除用户信息</view>
				</navigator>
			</view>

		</view>
	</view>
</template>

<script>   //这里是设置轮播图的地址，暂时用的静态资源，但实际上应该用get请求！
	export default {
		data() {
			return {
				swipers: []
			}
		},
		onLoad:function(){
			uni.request({
				url: 'http://8.142.82.195/viewforseller',
				method: 'GET',
				data: {},
				success: res => {this.swipers=res.data.data;console.log(this.swipers)},
				fail: () => {},
				complete: () => {}
			});
		},
		methods: {
			}
		}
</script>

<!-- scoped表示局部部署，scss是一种css的预处理语言，方便进行css编码 -->
<style lang="scss" scoped>
	page {
		max-height: 100%;
	}
	
	.banner-swiper {
		width: 100%;
		height: 600rpx;
		
		.banner-swiper-item {
			image {
				width: 100%;
			}
		}
	}
	
	.content {
		width: 100%;
		padding: 0 30rpx;
		position: relative;
	}
	
	.section-1 { //样式注册，设定形式
		position: relative;
		background-color: $bg-color-white;
		margin-top: -60rpx;
		border-radius: $border-radius-lg;
		padding: 60rpx 0;
		display: flex;
		margin-bottom: 30rpx;
		box-shadow: $box-shadow;
		
		.item {
			flex: 1;
			flex-shrink: 0;
			display: flex;
			flex-direction: column;
			align-items: center;
			position: relative;
			
			&:nth-child(1):after {
				content: '';
				position: absolute;
				right: 0;
				top: 0;
				bottom: 0;
				width: 2rpx;
				background-color: $border-color;
			}
			
			image {
				width: 100rpx;
				margin-bottom: 20rpx;
			}
			
			.wenyue-font {
				font-size: 48rpx;
				margin-bottom: 10rpx;
			}	
		}
	}
	
	.section-2 {
		display: flex;
		justify-content: space-between;
		margin-bottom: 30rpx;
		
		.item {
			width: 335rpx;
			background-color: #EAEBEC;
			padding: $spacing-row-lg 0;
			display: flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			border-radius: $border-radius-lg;
			
			.title {
				width: 100%;
				display: flex;
				align-items: center;
				justify-content: center;
				font-size: $font-size-lg;
				
				image {
					width: 60rpx;
					height: 60rpx;
					margin-right: 10rpx;
				}
			}
			
			.tips {
				color: $text-color-assist;
				font-size: $font-size-base;
			}
		}
	}
	
	.section-3 {
		margin-bottom: 30rpx;
		display: flex;
		justify-content: space-between;
		align-items: center;
		font-size: $font-size-base;
		color: $text-color-assist;
		padding: 0 10rpx;
		
		.my-integral {
			flex: 1;
			display: flex;
			flex-direction: column;
			
			.integrals {
				display: flex;
				align-items: center;
				font-size: $font-size-lg;
				color: $text-color-base;
				margin-bottom: 10rpx;
				
				.neutra-font {
					margin-left: 10rpx;
					font-size: 42rpx;
				}
			}
		}
		
		.my-code {
			display: flex;
			flex-direction: column;
			align-items: center;
			padding: 0 30rpx;
			position: relative;
			
			image {
				width: 60rpx;
				height: 60rpx;
				margin-bottom: $spacing-col-sm;
			}
			
			&:before {
				content: " ";
				position: absolute;
				left: 0;
				top: 0;
				bottom: 0;
				border-left: 1rpx solid rgba($color: $border-color, $alpha: 0.6);
			}
		}
	}
</style>
