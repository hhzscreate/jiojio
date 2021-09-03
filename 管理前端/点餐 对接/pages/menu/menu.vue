<template>
	<view class="container">
		<view class="address-form">
			<list-cell padding="30rpx">
				<view class="form-item">
					<image :src="url" mode="aspectFill"></image>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">菜名</view>
					<input type="text" v-model="name"  placeholder-class="placeholder"/>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">菜的描述</view>
					<input type="text" v-model="description"  placeholder-class="placeholder"/>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">价格</view>
					<input type="text" v-model="price"  placeholder-class="placeholder"/>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">能否单点</view>
					<radio-group @change="radioChange2">
								<label>
									<radio value="是" checked="checked" /><text>能</text>
									<radio value="否" /><text>不能</text>
								</label>
					</radio-group>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">是否外带</view>
					<radio-group @change="radioChange">
								<label>
									<radio value="是" checked="checked" /><text>可以带走</text>
									<radio value="否" /><text>不能带走</text>
								</label>
					</radio-group>
				</view>
			</list-cell>
			<list-cell padding="30rpx">
				<view class="form-item">
					<view class="label">新菜图片</view>
					<input type="text" v-model="url" placeholder="例:https://api//img" placeholder-class="placeholder"/>
				</view>
			</list-cell>
		</view>
		
		<view class="save-btn" @tap="setnewmenu" >
			<button type="info">确认修改</button>
		</view>
	</view>
</template>

<script>
	//用到了listCell
	import listCell from '@/components/list-cell/list-cell.vue'
	
	export default {
		components: {
			listCell
		},
		data() {
			return {
					name: '',
					description:'',
					is_single: '是',
					price: '',
					url:'',
					support_takeaway:'是',
					id:''
			}
		},
		onLoad:function(e){
			// var temp=e.newsid.img;
			this.name=e.name;
			this.description=e.description;
			this.price=e.price;
			this.url=e.img;
			this.id=e.diskid;
		},
		methods: {
				radioChange(e){
					this.support_takeaway=e.detail.value;
				},
				radioChange2(e){
					this.is_single=e.detail.value;
				},
				setnewmenu(){
					uni.request({
						url: 'http://8.142.82.195/altermenu',
						method: 'GET',
						data: {
							'name':this.name,
							'description':this.description,
							'is_single':this.is_single,
							'price':this.price,
							'url':this.url,
							'support_takeaway':this.support_takeaway,
							'id':this.id
						},
						success: res => {this.message=res.data.msg;console.log(this.message)
						uni.showToast({
							title: this.message,
							duration: 2000
						});
						},
						fail: () => {
							uni.showToast({
								title: "网络有问题！！",
								duration: 2000
							});
						},
						complete: () => {}
					});
					
				}
			}
		}
		
</script>

<style lang="scss" scoped>
.address-form {
	margin-top: 20rpx;
	
	.form-item {
		width: 100%;
		display: flex;
		align-items: center;
		
		.label {
			width: 160rpx;
		}
		
		input {
			flex: 1;
		}
		
		.jump-icon {
			width: 30rpx;
			height: 48rpx;
		}
		
		.radio {
			display: flex;
			margin-right: 50rpx;
			image {
				width: 40rpx;
				height: 40rpx;
				margin-right: 20rpx;
			}
		}
	}
}

.save-btn {
	padding: 0 30rpx;
	margin-top: 60rpx;
	
	button {
		width: 100%;
		font-size: $font-size-extra-lg;
	}
}
</style>
