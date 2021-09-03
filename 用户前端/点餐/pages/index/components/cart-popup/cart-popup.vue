<!-- 购物车的弹出 -->
<template>
	<!-- 父组件给子组件传递参数时用数据绑定如:title='title'(后面的就是父组件里面的data)，子组件用prop:['title']接收父组件的数据 -->
	<!-- 子组件给父组件传值则通过this.$emit('名字(这个是写在父组件标题里的，比如@myevent=，myevent就是emit传递的对象，然后myevent后面再绑定事件，可以触发父组件里的事件)') -->
	<uni-popup ref="popup" type="bottom" @change="change">
		<view class="cart-popup">
			<view class="header">
				<view class="order-type">
					<view class="font-weight-bold">门店订单</view>
					<view class="extra">自提/外送</view>
				</view>
				<view class="d-flex align-items-center" @tap="clear">
					<image src="/static/images/common/delete.png" class="delete-btn"></image>
					<view>清空购物车</view>
				</view>
			</view>
			<scroll-view scroll-y class="content">
				<view class="wrapper">
					<view class="list">
						<view class="item" v-for="(item, index) in cart" :key="index">
							<view class="left">
								<image :src="item.image" mode="widthFix" class="image"></image>
							</view>
							<view class="right">
								<view class="name-and-materials">
									<view class="name">{{ item.name }}</view>
									<view class="materials" v-if="item.materials_text">{{ item.materials_text }}</view>
								</view>
								<view class="price-and-actions">
									<view class="price">￥{{ item.price }}</view>
									<actions :number="item.number" @add="add(item)" @minus="minus(item)"></actions>
								</view>
							</view>
						</view>
					</view>
				</view>
			</scroll-view>
		</view>
	</uni-popup>
</template>

<script>
import uniPopup from '@/components/uni-popup/uni-popup.vue'
import actions from '../actions/actions.vue'

export default {
	//components中是要进行注册的自定义组件
	components: {
		uniPopup,   //意思即用的时候名字是uniPopup，实际也是
		actions
	},
	
	//接收来自父组件的数据
	//写成字典是因为这里的cart不是简单的数据类型，而是一个数组，需要这种形式注明type
	//因此这里接收的就是父组件（即用到了cart-popup这个组件的地方，看看有没有数据绑定的形式
	//比如:cart='cart'，即表示把购物车的列表传过来了
	props: {
		cart: {
			type: Array,
			default: () => []
		}
	},
	methods: {
		open() {
			this.$refs['popup'].open()
		},
		close() {
			this.$refs['popup'].close()
		},
		change({show}) {
			this.$emit('change', show)
		},
		add(item) {
			this.$emit('add', item)
		},
		minus(item) {
			this.$emit('minus', item)
		},
		
		//用于清空购物车的函数，在订单生成的时候需要用到！！！
		clear() {
			uni.showModal({
			    content: '清空购物车',
				confirmColor: '#DBA871',
			    success: res => {
					//如果点击了确认，则执行clear
			        if (res.confirm) {
						this.$emit('clear')
			        }
			    }
			})
		}
	}
};
</script>

<style lang="scss" scoped>
.cart-popup {
	background-color: $bg-color-white;
	padding-bottom: 100rpx;
}

.header {
	padding: 20rpx 30rpx;
	display: flex;
	justify-content: space-between;
	align-items: center;
	border-bottom: 1rpx solid rgba($color: $border-color, $alpha: 0.6);
	font-size: $font-size-sm;
	color: $text-color-assist;

	.order-type {
		display: flex;
		align-items: center;
		font-size: $font-size-sm;
		color: $text-color-base;
		
		.extra {
			margin-right: 10rpx;
			border: 2rpx solid $color-primary;
			font-size: 18rpx;
			padding: 2rpx 10rpx;
			color: $color-primary;
			margin-left: 10rpx;
		}
	}
	
	.delete-btn {
		width: 46rpx;
		height: 46rpx;
		margin-right: 10rpx;
	}
}

.content {
	max-height: calc(100vh - 600rpx);
	
	.wrapper {
		width: 100%;
		height: 100%;
		padding: 0 30rpx;
	}
	
	.list {
		display: flex;
		flex-direction: column;
		margin-bottom: 30rpx;
		
		.item {
			display: flex;
			align-items: stretch;
			padding: 30rpx 0;
			position: relative;
			
			&:after {
				content: ' ';
				position: absolute;
				bottom: 0;
				left: 180rpx;
				right: 0;
				border-bottom: 1rpx solid rgba($color: $border-color, $alpha: 0.6);
			}
			
			.left {
				flex-shrink: 0;
				display: flex;
				align-items: center;
				
				.image {
					width: 180rpx;
				}
			}
			
			.right {
				flex: 1;
				display: flex;
				flex-direction: column;
				justify-content: space-between;
				font-size: $font-size-medium;
				color: $text-color-base;
				
				.name-and-materials {
					display: flex;
					flex-direction: column;
					margin-bottom: 20rpx;
					
					.name {
						font-weight: bold;
					}
					
					.materials {
						font-size: $font-size-sm;
						color: $text-color-assist;
					}
				}
				
				.price-and-actions {
					display: flex;
					justify-content: space-between;
				
					.price {
						color: $text-color-grey;
					}
				}
			}
		}
	}
}
</style>
