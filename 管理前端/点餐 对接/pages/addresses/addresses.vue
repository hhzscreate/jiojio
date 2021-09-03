<template>
	<view class="container">
		<view class="content">
	
		</view>
		<view class="footer">
			<button type="info" @tap="add" open-type="navigate" url="pages//mart//mart">+添加新菜</button>
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
				
			}
		},
		computed: {
			...mapState(['addresses'])
		},
		methods: {
			...mapMutations(['SET_ADDRESS', 'SET_ORDER_TYPE']),
			add() {
				uni.navigateTo({
					url: '/pages/addresses/add'
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
