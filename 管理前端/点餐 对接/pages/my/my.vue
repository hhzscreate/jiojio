<template>
	<view class="container">
		<!-- 猜你喜欢 begin -->
		<view class="you-may-also-like">
			<navigator class="product" v-for="(product, index) in users":key='index' >				
					<view class="extra">
						<view class="action">
							
							<image :src="product.url" mode="aspectFill"></image>
							<view class="title"s>{{"用户id："}}{{product.userid}}</view>
							<view class="title">{{"用户名称："}}{{product.username }}</view>
							<view class="title">{{"电话号码："}}{{product.telphone }}</view>
							<view class="title">{{"性别："}}{{product.gender }}</view>
							<view class="title">{{"生日："}}{{product.birthday }}</view>
							
							<button type="primary" hover-class="none" @tap="del":data-newsid=product.userid >加入黑名单</button>
							<button type="default" hover-class="none" @tap='set(product.userid,product.username,product.birthday,product.telphone,product.url)'>修改用户信息</button>
						</view>
					</view>
			</navigator>
		</view>
		<!-- 猜你喜欢 end -->
		
		<nomore text="已经到底了,去其他页面逛逛吧" visible></nomore>
	</view>
</template>

<script>
	import nomore from '@/components/nomore/nomore.vue'
	
	export default {
		components: {
			nomore
		},
		data() {
			return {
				mart: [],
				messge:"",
				users:[]
			}
		},
		async onLoad() {
		uni.request({
			url: 'http://8.142.82.195/usersinfo',
			method: 'GET',
			data: {},
			success: res => {this.users=res.data.data;console.log(this.users)},
			fail: () => {},
			complete: () => {}
			});
		},
		onShow:function(){
			uni.request({
				url: 'http://8.142.82.195/usersinfo',
				method: 'GET',
				data: {},
				success: res => {this.users=res.data.data;console.log(this.users)},
				fail: () => {},
				complete: () => {}
				});
		},
		methods:{
			//删除用户
			del(e){
				var name=e.currentTarget.dataset.newsid;
				uni.request({
					url: 'http://8.142.82.195/deluser',
					method: 'GET',
					data: {'deluser':name},
					success: res => {console.log(res)
				
				},
					fail: () => {uni.showToast({
						title: '网络错误！！',
						duration: 2000
					});},
					complete: () => {}
				});
				uni.request({
					url: 'http://8.142.82.195/viewtodo',
					method: 'GET',
					data: {},
					success: res => {this.mart=res.data.data;this.messge=res;},
					fail: () => {},
					complete: () => {}
				});
				uni.showToast({
					title: '删除成功！！',
					duration: 2000
				});

			},
			set(id,username,birthday,telephone,url){
				console.log('点击')
				uni.navigateTo({
					url: '/pages/uses/uses?username='+username+"&birthday="+birthday+"&telephone="+telephone+"&url="+url+"&id="+id,
					success: res => {},
					fail: () => {},
					complete: () => {}
				});
			}
		}
	}
</script>

<style lang="scss">
	page {
		height: auto;
		
		/* #ifdef H5 */
		min-height: 100%;
		/* #endif */
	}
	
	.banner-swiper {
		height: 750rpx;
		
		.swier-item {
			image {
				height: 100%;
			}
		}
	}
	
	.banner-section {
		display: flex;
		background-color: #FFFFFF;
		
		image {
			width: 375rpx;
		}
	}
	
	.section-header {
		display: flex;
		align-items: baseline;
		padding: 20rpx 0;
		
		
		.subtitle {
			font-family: 'neutra';
			font-size: $font-size-sm;
			color: $text-color-assist;
		}
	}
	
	.content-section {
		background-color: #FFFFFF;
		padding: 0 30rpx;
	}
	.title {
		width: 100%;
		display: flex;
		// align-items: center;
		// justify-content: center;
		font-size: $font-size-lg;
	}
	.new-arrivals {
		margin-bottom: 20rpx;
		.section-body {
			display: flex;
			flex-direction: column;
			
			image {
				width: 100%;
				margin-bottom: 10rpx;
			}
		}
	}
	
	.you-may-also-like {
		padding: 20rpx 30rpx;
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		
		.product {
			background-color: #FFFFFF;
			width: 700rpx;
			display: flex;
			flex-direction: column;
			border-radius: $border-radius-lg;
			margin-bottom: 20rpx;
			
			image {
				width: 100%;
				border-radius: $border-radius-lg $border-radius-lg 0 0;
			}
			
			.info {
				padding: 20rpx;
				display: flex;
				flex-direction: column;
				overflow: hidden;
				
				.desc {
					display: flex;
					flex-direction: column;
					
					.title {
						font-size: $font-size-lg;
						overflow: hidden;
						text-overflow: ellipsis;
						white-space: nowrap;
						margin-bottom: 14rpx;
					}
					
					.sub {
						font-size: $font-size-sm;
						color: $text-color-assist;
					}
				}
				
				.extra {
					margin-top: 20rpx;
					display: flex;
					align-items: center;
					justify-content: space-between;
					
					.price {
						color: $color-primary;
						font-size: $font-size-lg;
						font-weight: 500 !important;
					}
					
					.action {
						image {
							width: 40rpx;
							height: 40rpx;
						}
					}
				}
			}
		}
	}
</style>
