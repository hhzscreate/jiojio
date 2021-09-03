<template>
	<view class="container">
		<view class="bg-white p-30 d-flex align-items-center justify-content-between mb-20">
			<view>
				<text class="mr-20">联系电话</text>
				<text>18666610000</text>
			</view>
			<button type="primary" plain class="font-size-sm line-height-1">自动填写</button>
		</view>
		<view class="bg-white p-30 mb-20">
			<view class="font-size-medium font-weight-bold mb-30">取餐时间</view>
			<view class="text-color-primary">【这里是后台人员传送的数据】</view>
		</view>
		<view class="bg-white pt-30 mb-20">
			<view class="font-size-medium font-weight-bold mb-30 pl-30">商品列表</view>
			<list-cell arrow line-right>
				<view class="w-100 d-flex align-items-center overflow-hidden">
					<scroll-view class="flex-fill overflow-hidden" scroll-x>
						<view class="w-100 d-flex align-items-center">
							<image :src="item.image" class="pro-img" v-for="(item, index) in cart" :key="index"></image>
						</view>
					</scroll-view>
					<view class="flex-shrink-0 ml-20">共{{ cartNum }}件</view>				
				</view>
			</list-cell>
			<list-cell arrow last>
				<view class="w-100 d-flex align-items-center justify-content-between">
					<view class="d-flex align-items-center">
						<view>优惠券</view>
						<view class="coupon-label">劵</view>
					</view>
					<view class="text-color-assist">暂无可用</view>
				</view>
			</list-cell>
			<list-cell arrow last>
				<view class="w-100 d-flex align-items-center justify-content-between overflow-hidden">
					<view class="flex-shrink-0">备注</view>
					<navigator hover-class="none" class="flex-fill ml-40 text-truncate text-right" open-type="navigate" url="/pages/pay/remark">{{ remark }}</navigator>
				</view>
			</list-cell>
			<list-cell last>
				<view class="w-100 d-flex justify-content-end align-items-center">
					<text class="font-size-sm">共{{ cartNum }}件商品，小计</text>
					<text class="font-size-lg font-weight-bold">￥{{ cartAmount }}</text>
				</view>
			</list-cell>
		</view>
		<list-cell last>
			<view class="w-100 d-flex align-items-center justify-content-between">
				<view>支付方式</view>
				<view class="d-flex align-items-center">
					<image src="/static/images/order/weixin-pay.png" class="wx-pay-icon"></image>
					<view>微信</view>
				</view>
			</view>
		</list-cell>
		<view class="footer">
			<view class="mr-30">
				合计：<text class="font-size-lg font-weight-bold">￥{{ cartAmount }}</text>
			</view>
			
			<!-- 点击支付后将会保存订单！！！！ -->
			<button type="primary" @click="saveOrder">支付</button>
		</view>
	</view>
</template>

<script>
	import listCell from '@/components/list-cell/list-cell.vue'
	
	export default {
		components: {
			listCell
		},
		data() {
			return {
				//这里已经拿到了cart！！！！
				//cart是一个列表，里面存的数据对象是字典，形式为：
				// {
				// 	id: product.id,
				// 	cate_id: product.category_id,
				// 	name: product.name,
				// 	price: product.price,
				// 	number: product.number || 1,   //如果没有
				// 	image: product.images[0].url,
				// 	is_single: product.is_single,
				// 	materials_text: product.materials_text || ''
				// }
				cart: uni.getStorageSync('cart'),
			}
		},
		computed: {
			cartNum() {
				return this.cart.reduce((acc, cur) => acc + cur.number, 0)
			},
			cartAmount() {
				return this.cart.reduce((acc, cur) => acc + cur.number * cur.price, 0)
			},
			remark() {
				return this.$store.state.remark
			}
		},
		methods:{
			saveOrder(){//将会生成一个订单并发送给后台保存，并且关闭当前页面返回菜单项
				//cart里面的每一项都是一种菜品，要先生成item数据保存，再生成order数据保存！无语
				var year=new Date().toString().slice(10,15)
				var hour=new Date().toString().slice(16,18)
				var minute=new Date().toString().slice(19,21)
				var second=new Date().toString().slice(22,24)
				var orderId=year+hour+minute+second
				for (let i of this.cart){
					uni.request({
						url:"http://8.142.82.195/setitemtest/",//接口地址
						data:{
							openId:getApp().globalData.openId,
							orderId:orderId,//菜单Id，能保证item里面的菜知道自己是哪份订单的,是唯一的
							sname:i.name,
							quantity:i.number
							//price:可以去数据库里找
							//image:也可以去数据库里找
							//total_fee:也可以在后台计算出来
						}
					})
				}
				
				var total_fee=this.cart.reduce((acc, cur) => acc + cur.number * cur.price, 0)
				var remarks=this.$store.state.remark
				//生成玩item后，开始请求生成order
				uni.request({
					url:"http://8.142.82.195/setordertest/",
					data:{
						total_fee:total_fee,
						remarks:remarks,
						payment:total_fee,
						//shopName:后台生成
						orderId:orderId,//要在前端就生成！！！是时间显示
						userName:"Tang",//用于后面的根据账号查找订单
						openId:getApp().globalData.openId
						//created_at:后台生成
						//payment：后台生成
					}
				})
				
				//开始关闭页面和购物车并返回订单页面
				uni.switchTab({
					url:'/pages/order/order'
				})
				
				// //触发全局事件
				// uni.$emit('cleatcart')
						
			}
		}
	}
</script>

<style lang="scss" scoped>
	.container {
		height: auto;
		padding-bottom: 120rpx;
	}
	
	.pro-img {
		width: 120rpx;
		height: 90rpx;
		flex-shrink: 0;
	}
	
	.coupon-label {
		background-color: $color-primary;
		color: #FFFFFF;
		font-size: 18rpx;
		line-height: 0.9rem;
		width: 0.9rem;
		height: 0.9rem;
		margin-left: 10rpx;
		text-align: center;
	}
	
	.wx-pay-icon {
		width: 40rpx;
		height: 40rpx;
		margin-right: 10rpx;
	}
	
	.footer {
		background-color: #FFFFFF;
		z-index: 10;
		position: fixed;
		bottom: 0;
		left: 0;
		width: 100%;
		height: 100rpx;
		display: flex;
		justify-content: flex-end;
		align-items: center;
		
		button {
			width: 250rpx;
			text-align: center;
			padding: 0;
			height: 100%;
			line-height: 100rpx;
			border-radius: 0 !important;
			font-size: $font-size-lg;
		}
	}
</style>
