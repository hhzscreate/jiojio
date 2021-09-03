<!-- 这里一直都默认gender为1！！！ -->
<template>
	<view class="container">
		<view class="content">
			
			<!-- v-for中的address是需要值data中定义的，因此在下面的view中可以直接使用 -->
			<list-cell v-for="(address, index) in addresses" :key="index" :line-left="false" @tap="choose(address)">
				<view class="address">
					<view class="info">
						<view class="user-row">
							{{ `${address.name}(${address.gender ? '女士' : '男士'}) ${address.phone}` }}
						</view>
						<view class="address-row">
							<!-- 只有当是默认地址的时候才显示 -->
							<!-- 在v-for循环中，每个都要判断 -->
							<view class="is-default" v-show="address.is_default">默认地址</view>
							<view class="address">{{ `${address.address} ${address.description}` }}</view>
						</view>
					</view>
					<image src="/static/images/common/edit.png" @tap.stop="edit(address.id)" class="edit-btn"></image>
				</view>
			</list-cell>
		</view>
		<view class="footer">
			<button type="info" @tap="add">+添加地址</button>
		</view>
	</view>
</template>

<script>
	import listCell from '@/components/list-cell/list-cell.vue'
	import {mapState, mapMutations} from 'vuex'
	
	export default {
		components: {
			listCell
		},
		data() {
			return {
				addresses:[],
				// orderType: 'takein',
				address:{}
			}
		},
		// computed: {
		// 	//这里获取了addresses数据，addresses数据应该和userName或者openid有关
		// 	...mapState(['addresses'])
		// },
		
		//实际的初始化应该在这里
		//出错的原因：返回的res.data不是列表！res.data.data才会返回res.data的真正格式
		async onLoad(){
			const res=await this.$myRequest({
				url:'/getadressestest/',
				data:{
					user_id:getApp().globalData.openId
				}
			})
			this.addresses=res.data.data
			// console.log(res.data.data)
			//console.log(this.addresses)
		},
		async onShow(){
			const res=await this.$myRequest({
				url:'/getadressestest/',
				data:{
					user_id:getApp().globalData.openId
				}
			})
			this.addresses=res.data.data
			// console.log(res.data.data)
			//console.log(this.addresses)
		},
		
		
		methods: {
			// 直接获取了方法
			//...mapMutations(['SET_ADDRESS', 'SET_ORDER_TYPE']),
			add() {
				uni.navigateTo({
					url: '/pages/addresses/add'
				})
			},
			//这里的id是address的id，指向是哪一条收货地址
			edit(id) {
				uni.navigateTo({
					url: '/pages/addresses/set?id=' + id
				})
			},
			set_address(address){
				this.address=address
			},
			// set_order_type(orderType){
			// 	this.orderType = orderType
			// },
			
			//选定当前地址
			choose(address) {		
				this.set_address(address)
				//这里应该调用上一个页面的函数
				// var pages = getCurrentPages();
				// var prevPage = pages[pages.length - 2]; //上一个页面
				// prevPage.set_order_type('takeout')
				// prevPage.set_address(address)//传给上一个页面
				
				getApp().globalData.orderType='takeout'
				getApp().globalData.address=address
				//this.set_order_type('takeout')
				uni.switchTab({
					url: '/pages/index/index'
				})
			}
		}
	}
</script>

<style lang="scss" scoped>
	.content {
		height: auto;
		margin-top: 20rpx;
		padding-bottom: 170rpx;
	}
	
	.address {
		width: 100%;
		display: flex;
		align-items: center;
		
		.info {
			flex: 1;
			display: flex;
			flex-direction: column;
			margin-right: 20rpx;
			overflow: hidden;
			
			.user-row {
				font-size: $font-size-lg;
				font-weight: 500;
				margin-bottom: 10rpx;
			}
			
			.address-row {
				display: flex;
				align-items: center;
				
				.is-default {
					background-color: #faf5ef;
					font-size: 16rpx;
					color: $color-primary;
					padding: 4rpx;
					flex-shrink: 0;
					margin-right: 6rpx;
				}
				
				.address {
					font-size: $font-size-base;
					overflow: hidden;
					white-space: nowrap;
					text-overflow: ellipsis;
				}
			}
		}
		
		.edit-btn {
			width: 45rpx;
			height: 45rpx;
			margin-right: 20rpx;
		}
	}
	
	.footer {
		position: fixed;
		bottom: 0;
		width: 100%;
		z-index: 10;
		background-color: $bg-color;
		display: flex;
		align-items: center;
		justify-content: center;
		height: 150rpx;
		padding: 0 30rpx;
		
		button {
			width: 100%;
			font-size: $font-size-extra-lg;
		}
	}
</style>
