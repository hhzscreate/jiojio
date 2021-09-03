<template>
	<view class="container">
		<view class="navbar">
			<button type="default" plain class="talk-btn">
				<image src="/static/images/order/order_icon_talk2.0.png"></image>
				<view>接单系统</view>
			</button>
		</view>
		<view class="tabbar">
			<view class="item" :class="{active: !tabIndex}" @tap="switchTab(0)">所有待处理订单</view>
			
			<!-- <view class="item" :class="{active: tabIndex}" @tap="switchTab(1)">历史订单</view> -->
		</view>
		<swiper :current="tabIndex" :duration="300" class="swiper" :show-scrollbar="false">
			
			<!-- 当前订单 begin -->
			<swiper-item @touchmove.stop="handleSwiperItemChange">
				<view class="history-order">
					<view class="menu">
						<view class="flex-fill d-flex justify-content-start">
							<view class="item" :class="{active: !orderMenuIndex}" @tap="switchMenuTab(0)">待接单</view>
							<view class="item" :class="{active: orderMenuIndex}" @tap="switchMenuTab(1)">待完成</view>
						</view>
						
						<!-- 当数量足够的时候才能开批量的发票 -->
						<view class="item" v-show="batchInvoiceVisible">
							<image src="/static/images/order/batch_invoice_icon.png"></image>
							<view>批量开票</view>
						</view>
					</view>
					
					<!-- :current="orderMenuIndex" :duration="300" :show-scrollbar="false"都是数据绑定
					是当前页面传给swiper的数据，比如令swiper的current等于当前页面中的orderMenuIndex-->
					
					<swiper :current="orderMenuIndex" :duration="300" :show-scrollbar="false" class="history-order-swiper">
						<!-- 门店订单 begin -->
						<swiper-item @touchmove.stop="handleSwiperItemChange">
							
							
							<view class="store-order-wrapper" v-show="isEmpty" @tap="tiaozhuan()">
								<image src="/static/images/order/default_img_order.png"></image>
								<view>您还没有下单</view>
								<view>快去菜单逛逛吧</view>
							</view>
							
							<scroll-view scroll-y="true" class="orders-scroll">
								
								<view class="wrapper">
									
									<view class="order-list">
										
										<!-- 对于每一个order绑定了一个跳转按钮，按下去可以跳转到订单的商品详情
										测试数据里使用的是静态数据，现实中应该是将数据库中的订单读出来，取里面的数据来进行展示 -->
										<!-- <navigator class="order" v-for="(order, index) in orders" :key="index" open-type="navigate" :url="'/pages/order/detail?id=' + order.id"> -->
										
										<!-- 测试怎么传递参数 -->
										<navigator class="order" v-for="(order, index) in orders" :key="index" open-type="navigate" :url="'/pages/pay/pay?order=' + encodeURIComponent(JSON.stringify(order))">
											
											<!-- 目前看来order里面需要的内容：
											name商店名字 -->
											<view class="header">
												<view class="flex-fill font-size-medium">{{ order.shopName }}</view>
												<view class="status">
													<view>待接单</view>
													<image src="/static/images/common/black_arrow_right.png"></image>
												</view>
											</view>
											
											<!-- 还需要items，即购物车列表，items里面有图片数据读出来展示 -->
											<scroll-view scroll-x>
												<view class="images">
													<image :src="item.image" v-for="(item, index) in order.items" :key="index"></image>
												</view>
											</scroll-view>
											
											<!-- 还需要下单时间created_at，总价格total_fee -->
											<view class="info">
												<view class="left">
													<!-- <view>订单编号：{{ order.no }}</view> -->
													<view>下单时间：{{ order.created_at }}</view>
												</view>
												<view class="right">
													￥{{ order.total_fee }}
												</view>
											</view>
											
											<view class="action">
												
												<!-- @tap.stop后面接的事件将不会冒泡 -->
												<!-- 去detail删除订单！ -->
												<!-- <button type="default" hover-class="none" @tap.stop="deleteorder(order)">删除记录</button> -->
												<button type="default" hover-class="none">开发票</button>
												<button type="primary" plain hover-class="none" @tap.stop="jiedang(order.allid)">接单</button>
											</view>
										</navigator>
									</view>
								</view>
							</scroll-view>
						</swiper-item>
						<!-- 门店订单 end -->
						
						
						<!-- 百货订单 begin -->
						<swiper-item @touchmove.stop="handleSwiperItemChange">
							
							
							<view class="store-order-wrapper" v-show="isEmpty" @tap="tiaozhuan()">
								<image src="/static/images/order/default_img_order.png"></image>
								<view>还没有待完成订单</view>
								<view>快去接单吧</view>
							</view>
							
							<scroll-view scroll-y="true" class="orders-scroll">
								
								<view class="wrapper">
									
									<view class="order-list">
										
										<!-- 对于每一个order绑定了一个跳转按钮，按下去可以跳转到订单的商品详情
										测试数据里使用的是静态数据，现实中应该是将数据库中的订单读出来，取里面的数据来进行展示 -->
										<!-- <navigator class="order" v-for="(order, index) in orders" :key="index" open-type="navigate" :url="'/pages/order/detail?id=' + order.id"> -->
										
										<!-- 测试怎么传递参数 -->
										<navigator class="order" v-for="(order, index) in orders2" :key="index" open-type="navigate" :url="'/pages/pay/pay?order=' + encodeURIComponent(JSON.stringify(order))">
											
											<!-- 目前看来order里面需要的内容：
											name商店名字 -->
											<view class="header">
												<view class="flex-fill font-size-medium">{{ order.shopName }}</view>
												<view class="status">
													<view>待完成</view>
													<image src="/static/images/common/black_arrow_right.png"></image>
												</view>
											</view>
											
											<!-- 还需要items，即购物车列表，items里面有图片数据读出来展示 -->
											<scroll-view scroll-x>
												<view class="images">
													<image :src="item.image" v-for="(item, index) in order.items" :key="index"></image>
												</view>
											</scroll-view>
											
											<!-- 还需要下单时间created_at，总价格total_fee -->
											<view class="info">
												<view class="left">
													<!-- <view>订单编号：{{ order.no }}</view> -->
													<view>下单时间：{{ order.created_at }}</view>
												</view>
												<view class="right">
													￥{{ order.total_fee }}
												</view>
											</view>
											
											<view class="action">
												
												<!-- @tap.stop后面接的事件将不会冒泡 -->
												<!-- 去detail删除订单！ -->
												<!-- <button type="default" hover-class="none" @tap.stop="deleteorder(order)">删除记录</button> -->
												<button type="default" hover-class="none">开发票</button>
												<button type="primary" plain hover-class="none" @tap.stop="finish(order.allid)">完成订单</button>
											</view>
										</navigator>
									</view>
								</view>
							</scroll-view>
						</swiper-item>
						<!-- 百货订单 end -->
					</swiper>
				</view>
			</swiper-item>
			<!-- 当前订单 end -->
			
			
		</swiper>
	</view>
</template>

<script>
export default {
	data() {
		return {
			tabIndex: 0,
			orderMenuIndex: 0,
			orders: [],
			orders2:[],
			storeOrders: [],
			isEmpty:true,// 默认为空订单
			isEmpty2:true,// 默认为空订单
		}
	},
	async onLoad() {
		uni.request({
					url: 'http://8.142.82.195/ordertobegin',
					method: 'GET',
					success: res => {this.orders=res.data.data;},
					fail: () => {},
					complete: () => {}
				});
				uni.request({
					url: 'http://8.142.82.195/ordertofinish',
					method: 'GET',
					success: res => {this.orders2=res.data.data;},
					fail: () => {},
					complete: () => {}
		});
		if(this.orders.length){//如果购物车为空，则显示您还没有下单这个view(默认false)
			this.isEmpty=false
		}
		else{
			this.isEmpty=true // 删完了后再次显示
		}
		if(this.orders2.length){//如果购物车为空，则显示您还没有下单这个view(默认false)
			this.isEmpty2=false
		}
		else{
			this.isEmpty2=true // 删完了后再次显示
		}
		
		//console.log(this.orders)
	},
	async onShow(){
		uni.request({
					url: 'http://8.142.82.195/ordertobegin',
					method: 'GET',
					success: res => {this.orders=res.data.data;},
					fail: () => {},
					complete: () => {}
				});
		uni.request({
					url: 'http://8.142.82.195/ordertofinish',
					method: 'GET',
					success: res => {this.orders2=res.data.data;},
					fail: () => {},
					complete: () => {}
		});
		//console.log(this.orders)
		if(this.orders.length){//如果购物车为空，则显示您还没有下单这个view(默认false)
			this.isEmpty=false
		}
		else{
			this.isEmpty=true // 删完了后再次显示
		}
		if(this.orders2.length){//如果购物车为空，则显示您还没有下单这个view(默认false)
			this.isEmpty2=false
		}
		else{
			this.isEmpty2=true // 删完了后再次显示
		}
	},
	computed: {
		batchInvoiceVisible() {
			var temp_0=0
			var temp_1=0
			if(this.orders){
				temp_0=this.orders.length
			}
				
				
			if(this.storeOrders){
				temp_0=this.storeOrders.length	
			}
				
			return (!this.orderMenuIndex && temp_0) || (this.orderMenuIndex && temp_1)
		}
	},
	methods: {
		jiedang(id){
			uni.request({
				url: 'http://8.142.82.195/beginoder',
				method: 'GET',
				data: {'id':id},
				success: res => {},
				fail: () => {},
				complete: () => {}
			});
			uni.request({
						url: 'http://8.142.82.195/ordertobegin',
						method: 'GET',
						success: res => {this.orders=res.data.data;},
						fail: () => {},
						complete: () => {}
					});
			uni.request({
						url: 'http://8.142.82.195/ordertofinish',
						method: 'GET',
						success: res => {this.orders2=res.data.data;},
						fail: () => {},
						complete: () => {}
			});
			uni.showToast({
				title: '接单成功！！',
				duration: 2000
			});
			//console.log(this.orders)
			if(this.orders.length){//如果购物车为空，则显示您还没有下单这个view(默认false)
				this.isEmpty=false
			}
			else{
				this.isEmpty=true // 删完了后再次显示
			}
			if(this.orders2.length){//如果购物车为空，则显示您还没有下单这个view(默认false)
				this.isEmpty2=false
			}
			else{
				this.isEmpty2=true // 删完了后再次显示
			}
		},
	finish(id){
		console.log(id)
		uni.request({
			url: 'http://8.142.82.195/finishoder',
			method: 'GET',
			data: {'id':id},
			success: res => {},
			fail: () => {},
			complete: () => {}
		});
		uni.request({
					url: 'http://8.142.82.195/ordertobegin',
					method: 'GET',
					success: res => {this.orders=res.data.data;},
					fail: () => {},
					complete: () => {}
				});
		uni.request({
					url: 'http://8.142.82.195/ordertofinish',
					method: 'GET',
					success: res => {this.orders2=res.data.data;},
					fail: () => {},
					complete: () => {}
		});
		uni.showToast({
			title: '完成订单！！',
			duration: 2000
		});
		//console.log(this.orders)
		if(this.orders.length){//如果购物车为空，则显示您还没有下单这个view(默认false)
			this.isEmpty=false
		}
		else{
			this.isEmpty=true // 删完了后再次显示
		}
		if(this.orders2.length){//如果购物车为空，则显示您还没有下单这个view(默认false)
			this.isEmpty2=false
		}
		else{
			this.isEmpty2=true // 删完了后再次显示
		}
	},
		async switchTab(index) {
			if(this.tabIndex === index) return
			this.tabIndex = index
			if(this.tabIndex) {
				await this.getOrders()
			}
		},
		handleSwiperItemChange() {	//禁止手动滑动
			return true
		},
		async switchMenuTab(index) {
			if(this.orderMenuIndex === index) return
			this.orderMenuIndex = index
			await this.getOrders()
		},
		
		//这里进行数据的传递
		async getOrders() {
			if(!this.orderMenuIndex) {
				uni.request({
							url: 'http://8.142.82.195/ordertobegin',
							method: 'GET',
							success: res => {this.orders=res.data.data;},
							fail: () => {},
							complete: () => {}
						});
			} else {
				//this.storeOrders = await this.$api('storeOrders')
			}
			
			
		},
		tiaozhuan(){
			console.log('点击')
		},
		
		//删除整个订单列表中的一个数据项
		//首先apii返回的是该账号的所有订单，是一个列表，我们要找到
		//进入详情页是因为他把那整个订单返回给detail页面进行了初始化
		//order是一个字典，里面可以取到很多信息
		// async deleteorder(order){
		// 	var openId=getApp().globalData.openId  //  openId是当前的
		// 	var orderId=order.orderId   // 再获取一个orderId即可
			
		// 	console.log(orderId)
			
		// 	const res=await this.$myRequest({
		// 		url:'/deleteordertest/',
		// 		data:{
		// 			"openId":openId,//去寻找需要
		// 			"orderId":orderId, //同上					
		// 		}
		// 	})
			
			
		// }
	}
};
</script>

<style lang="scss" scoped>
page {
	background-color: #f6f6f6;
}
.navbar {
	height: calc(44px + var(--status-bar-height));
	/* #ifdef H5 */
	height: 44px;
	/* #endif */
	display: flex;
	background-color: #FFFFFF;
}

.talk-btn {
	height: 32px;
	margin-left: 10px;
	margin-top: 26px;
	/* #ifdef H5 */
	margin-top: 6px;
	/* #endif */
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: $font-size-sm !important;
	padding: 0 20rpx;
	border-radius: 50rem !important;
	
	image {
		width: 40rpx;
		height: 40rpx;
		margin-right: $spacing-row-sm;
	}
}

.tabbar {
	height: 100rpx;
	background-color: $bg-color-white;
	display: flex;
	align-items: center;
	justify-content: space-around;
	
	.item {
		height: 100%;
		font-size: $font-size-lg;
		color: $text-color-assist;
		font-weight: 400 !important;
		display: flex;
		align-items: center;
		
		&.active {
			color: $text-color-base;
			border-bottom: 4rpx solid $text-color-base;
		}
	}
}

.swiper {
	width: 100%;
	height: calc(100vh - 44px - var(--status-bar-height) - 110rpx);
	/* #ifdef H5 */
	height: calc(100vh - 44px - var(--status-bar-height) - 110rpx - 100rpx);
	/* #endif */
}

.no-order-content {
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;

	image {
		width: 300rpx;
		height: 300rpx;
		margin-bottom: 50rpx;
	}

	.tips {
		color: $text-color-assist;
		display: flex;
		flex-direction: column;
		align-items: center;
		line-height: 1.2rem !important;
		margin-bottom: 70rpx;
	}

	button {
		width: 50%;
	}
}

.history-order {
	width: 100%;
	height: 100%;
	position: relative;
	
	.menu {
		padding: 18rpx 30rpx;
		display: flex;
		align-items: center;
		font-size: $font-size-base;
		color: $text-color-grey;
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		z-index: 10;
		
		.item {
			padding: 14rpx 30rpx;
			display: flex;
			align-items: center;
			justify-content: center;
			
			image {
				width: 40rpx;
				height: 40rpx;
				margin-right: 10rpx;
			}
			
			&.active {
				color: $color-primary;
				background-color: $bg-color-white;
			}
		}
	}
	
	.history-order-swiper {
		width: 100%;
		height: 100%;
	}
}

.store-order-wrapper {
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: center;
	font-size: $font-size-base;
	color: $text-color-assist;
	line-height: 1.3rem !important;
	
	image {
		width: 400rpx;
		height: 333rpx;
		margin-bottom: 40rpx;
	}
}

.orders-scroll {
	width: 100%;
	height: 100%;
	padding-top: 104rpx;
}

.order-list {
	display: flex;
	width: 100%;
	flex-direction: column;
	
	.order {
		background-color: $bg-color-white;
		padding: 30rpx 40rpx;
		margin-bottom: 18rpx;
		
		.header {
			display: flex;
			justify-content: space-between;
			align-items: center;
			
			.status {
				font-size: $font-size-base;
				color: $text-color-grey;
				display: flex;
				align-items: center;
				image {
					width: 30rpx;
					height: 30rpx;
					margin-left: $spacing-row-sm;
				}
			}
		}
		
		.images {
			display: flex;
			padding: 30rpx 0;
			image {
				flex-shrink: 0;
				width: 150rpx;
				height: 112.5rpx;
			}
		}
		
		.info {
			display: flex;
			align-items: center;
			margin-bottom: 30rpx;
			
			.left {
				flex: 1;
				display: flex;
				flex-direction: column;
				font-size: $font-size-base;
				color: $text-color-grey;
			}
			
			.right {
				font-size: $font-size-lg;
				color: $text-color-base;
			}
		}
		
		.action {
			display: flex;
			justify-content: flex-end;
			align-items: center;
			
			button {
				margin-left: 30rpx;
				font-size: $font-size-sm;
			}
		}
	}
}
</style>
