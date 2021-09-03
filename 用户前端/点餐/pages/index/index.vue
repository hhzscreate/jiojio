<template>
	<view class="container">  <!-- 是个容器类，有container抱在一起的在大屏幕上才能显示居中的-->
		<view class="header">
			
			<!-- 搜索栏 begin -->
			<!-- serch-box和serch-input都是在header下面自定义的 -->
			<view class="search-box">
				<!-- tap响应的是手指触摸事件，click是点击，@实际上就是v-on，进行事件绑定 -->
				<!-- 后面接的就是事件，事件应该在methods中进行注册 -->
				<!-- 这里改变的showSearch是data中的一个变量，赋值相当于简写一个函数 -->
				
				<!-- 具体怎么操作未知！！！ -->
				<view class="search-input" @click="showSearch=true">
					<image src="/static/images/common/search-icon.png" class="search-icon"></image>
					<view>搜索</view>
				</view>
			</view>
			<!-- 搜索栏 end -->
			
			<view class="center">
				<view class="store">
					<view class="title">
						<image :src="orderType == 'takein' ? 
								'/static/images/common/star_normal.png' : 
								'/static/images/order/order_icon_address.png'" 
								class="left-icon" />
						<view class="address">{{ orderType == 'takeout' ? address.complete_address : '来福士店' }}</view>
						<image src="/static/images/common/black_arrow_right.png" class="right-icon"></image>
					</view>
					
					
					<!-- 外卖&自取switch begin -->
					<view class="buttons">
						<button type="default" class="button" 
								:class="{active: orderType == 'takein'}" plain 
								hover-class="none" @click="switchOrderType">
							自取
						</button>
						<button type="default" class="button" 
								:class="{active: orderType == 'takeout'}" plain 
								hover-class="none" @click="switchOrderType">
							外卖
						</button>
					</view>
					<!-- 外卖&自取switch end -->
					
					
				</view>
				
				<view class="location">距离您1.2km</view>		
			</view>	
		</view>
		
		
		
		<view class="main">
			<!-- 左侧菜单 begin -->
			<scroll-view class="menu-bar" scroll-y scroll-with-animation>
				<view class="wrapper">
					
					<!-- 根据菜品里面的category.id来判断选择的属于哪一列 -->
					<view class="menu-item" @click="handleMenuSelected(category.id)" 
						  :class="{active: currentCategoryId == category.id}" v-for="(category, index) in categories" :key="index">
						<!-- <image:src="category.category_image_url" class="image" mode="widthFix"></image> -->
						<view class="title">{{ category.name }}</view>
					</view>
				</view>
				
				
			</scroll-view>
			<!-- 左侧菜单 end -->
			
			
			<!-- 右侧商品列表 begin -->
			<!-- scroll-view是一个组件，:scroll-top="productsScrollTop"设定滑动条的顶部为当前左侧点击的(属性绑定)
			 @scroll="productsScroll"触发事件使得右侧滑动栏滑动 -->
			<scroll-view class="product-section" scroll-y scroll-with-animation :scroll-top="productsScrollTop" @scroll="productsScroll">
				<view class="wrapper">
					<!-- 商品 begin -->
					<!-- 用for循环展示 -->
					
					<!-- categories是data,category, index是他里面数据项的属性 -->
					<!-- 从数据中取项目，category是一个完整的比如盖饭的全部，index是他的下标 -->
					<view class="products-list" v-for="(category, index) in categories" :key="index" :id="`products-${category.id}`">
						
						<!-- 展示属于左侧菜单栏的什么分类 -->
						<view class="category-name">{{ category.name }}</view>
						
						<view class="products">
							<!-- 展示当前category下面的所有的商品，比如盖饭的products有哪些，且附加点击触发详情页面事件 -->
							<view class="product" v-for="(product, key) in category.products" :key="key" 
								@click="showProductDetailModal(product)">
								
								<!-- 展示食物图片 -->
								<image :src="product.images[0].url" mode="widthFix" class="image"></image>
								
								
								<view class="content">
									<!-- 未知作用 -->
									<view class="name">{{ product.name }}</view>
																
									<!-- 还是描述标签，内容来自于json -->
									<!-- <view class="labels">
										<view class="label" 
										:style="{color: label.label_color, background: $util.hexToRgba(label.label_color, 0.2)}"
										 v-for="label in product.labels" :key="label.id">{{ label.name }}</view>
									</view> -->
									
									<!-- 描述标签 -->
									<view class="description">{{ product.description }}</view>
									
									<!-- 价格标签 -->
									<view class="price">
										<view>￥{{ product.price }}</view>
										
										<!-- 加号按钮，是一个自定义的组件，去component中去找！ -->
										<!-- product.is_single是一个函数，根据结果（购物车是否为空）去判断做什么操作 -->
										<!-- 功能分别是：点击图片显示详情， 购物车的数量，加入购物车，等等 -->
										<actions :materials-btn="!product.is_single" 
												@materials="showProductDetailModal(product)"  
												:number="productCartNum(product.id)"   
												@add="handleAddToCart(product)" 
												@minus="handleMinusFromCart(product)" />
									</view>
								</view>
							</view>
						</view>
					</view>
					<!-- 商品 end -->
				</view>
			</scroll-view>
			<!-- 右侧商品列表 end -->
		</view>
		
		
		<!-- 商品详情 modal begin -->
		<!-- <product-modal是一个自定义的组件,用于展示商品详情,具体情况在index目录下的components中> -->
		<product-modal :product="product" 
						:visible="productModalVisible" 
						@cancel="closeProductDetailModal" 
						@add-to-cart="handleAddToCartInModal" 
		/>
		<!-- 商品详情 modal end -->
		
		
		<!-- 购物车栏 begin -->
		<!-- 同上，自定义组件 -->
		
		<!-- 注意！这里的:cart="cart" 已经把购物车的列表传递下去了 -->
		<cart-bar :cart="cart" 
				  @add="handleAddToCart" 
				  @minus="handleMinusFromCart"
				  @clear="clearCart"
				  @pay="pay"
		/>
		<!-- 购物车栏 end -->
		
		<!-- 自定义组件 -->
		<search :show="showSearch" :categories="categories" @hide="showSearch=false" @choose="showProductDetailModal"></search>
	</view>
</template>

<script>
	import {mapState, mapMutations} from 'vuex'
	import Actions from './components/actions/actions.vue'
	import CartBar from './components/cartbar/cartbar.vue'
	import ProductModal from './components/product-modal/product-modal.vue'
	import cartPopup from './components/cart-popup/cart-popup.vue'
	import Search from './components/search/search.vue'
	
	
	export default {
		// 自定义组件说明
		components: {
			Actions,
			CartBar,
			ProductModal,
			cartPopup,
			Search
		},
		data() {
			return {
				categories:[], 
				cart: [],     //购物车！！！
				product: {},
				currentCategoryId: 0,
				notices: [],
				productModalVisible: false,
				cartPopupShow: false,
				productsScrollTop: 0,
				showSearch: false,
				// test:0
				isLogin:false,
				orderType:'takein',
				address:{}
			}
		},
		computed: {
			//...mapState(['orderType', 'address']),
			productCartNum() {	//计算单个饮品添加到购物车的数量
				//reduce是个累加器，acc是需要返回的，cur是当前元素，cart是一个列表，cur指向cart
				return id => this.cart.reduce((acc, cur) => {
						if(cur.id === id) {
							return acc += cur.number
						}
						return acc
					}, 0)
			}
		},
		async onLoad() {
			var that=this
			//this.notices = await this.$api('notices')
		
			//引入自己文件夹中的json数据!!!
			//this.categories = await this.$api('categories')
			
			
			//重要！！！！！！！
			//为什么会出错，因为res.data直接赋值的格式是object，但是我们需要的是列表的形式
			const res= await this.$myRequest({url:'/api/'})
			//console.log(res)
			//如果直接返回的json就用列表push
			// this.categories.push(res.data)
			// this.test=66
			
			this.categories=res.data.data
			this.address=getApp().globalData.address
			this.orderType=getApp().globalData.orderType
			
			//console.log(this.categories)
			//console.log(this.test)
			
			this.currentCategoryId = this.categories.length && this.categories[0].id
			this.isLogin=getApp().globalData.isLogin
			this.$nextTick(() => this.calcSize())
		},
		
		//从下级页面返回的时候会清空购物车
		//偷个懒先这些做
		onShow(){
			this.isLogin=getApp().globalData.isLogin
			this.clearCart()
			this.address=getApp().globalData.address
			this.orderType=getApp().globalData.orderType
		},
		
		methods: {
			
			//...mapMutations(['SET_ORDER_TYPE']),
			
			// getshishi(){
			// 	console.log('获取shishi的数据')
			// 	uni.request({
			// 		url:"http://127.0.0.1:8000/api/",
			// 		success: res=>{
			// 			console.log(res.data)
			// 			this.categories = res.data
			// 			console.log(this.categories)
			// 		},
			// 		fail: err=>{
			// 			uni.showToast({
			// 				title:"请求失败...",
			// 				icon:"none"
			// 			})
			// 			console.log(err)
			// 		}

			// 	})
			// },
			
			// async getshishi(){
			// 	const res= await this.$myRequest({
			// 		url:'/api/'
			// 	})
			// 	console.log(res)
			// 	this.categories=res.data
			// },
			// set_address(address){
			// 	this.address=address
			// },
			
			set_order_type(ordertype){
				this.orderType=ordertype
			},
			
			switchOrderType() {
				// if(this.isLogin){
				// 	if(this.orderType === 'takein') {
				// 		uni.navigateTo({
				// 			url: '/pages/addresses/addresses'
				// 		})
				// 	} else {
				// 		this.SET_ORDER_TYPE('takein')
				// 	}
				// }
				if(this.isLogin){
					if(this.orderType === 'takein') {
						uni.navigateTo({
							url: '/pages/addresses/addresses'
						})
					} else {
						this.set_order_type('takein')
					}
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
			handleAddToCart(product) {	//添加到购物车
				const index = this.cart.findIndex(item => {
					if(!product.is_single) {
						return (item.id == product.id) && (item.materials_text == product.materials_text)
					} else {
						return item.id === product.id
					}
				})
				
				if(index > -1) {
					this.cart[index].number += (product.number || 1)
					return
				}
				
				this.cart.push({
					id: product.id,
					cate_id: product.category_id,
					name: product.name,
					price: product.price,
					number: product.number || 1,
					image: product.images[0].url,
					is_single: product.is_single,
					materials_text: product.materials_text || ''
				})
			},
			handleMinusFromCart(product) { //从购物车减商品
				let index
				if(product.is_single) {
				   index = this.cart.findIndex(item => item.id == product.id)
				} else {
				   index = this.cart.findIndex(item => (item.id == product.id) && (item.materials_text == product.materials_text))
				}
				this.cart[index].number -= 1
				if(this.cart[index].number <= 0) {
					this.cart.splice(index, 1)
				}
			},
			showProductDetailModal(product) {//显示购物车组件，未登录则不显示
				if(this.isLogin){
					this.product = product
					this.productModalVisible = true
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
			handleAddToCartInModal(product) {
				this.handleAddToCart(product)
				this.closeProductDetailModal()
			},
			closeProductDetailModal() {
				this.productModalVisible = false
				this.product = {}
			},
			openCartDetailsPopup() {
				this.$refs['cartPopup'].open()
			},
			clearCart() {
				this.cart = []
			},
			// 改变左侧菜单栏的选中状态
			handleMenuSelected(id) {
				//点击左侧栏，传入id，去categories里面找到一个id与当前点击相同的那一项(比如点了盖饭，则去找盖饭的id)
				this.productsScrollTop = this.categories.find(item => item.id == id).top
				this.$nextTick(() => this.currentCategoryId = id)
			},
			productsScroll({detail}) {
				const {scrollTop} = detail
				let tabs = this.categories.filter(item=> item.top <= scrollTop).reverse()
				if(tabs.length > 0){
					this.currentCategoryId = tabs[0].id
				}
				//console.log(this.currentCategoryId)
				//显示未定义，又是this的指向问题！！！
				//console.log(this.productsScrollTop)
			},
			
			// 不知道拿来干嘛的,但最好别注释
			calcSize() {
				let h = 0
				let view = uni.createSelectorQuery().select('#ads')
				view.fields({
					size: true
				}, data => {
					h += data?Math.floor(data.height):0
					// h += Math.floor(data.height)
				}).exec()
				
				this.categories.forEach(item => {
					let view = uni.createSelectorQuery().select(`#products-${item.id}`)
					view.fields({
						size: true
					}, data => {
						item.top = h
						// let h = rect?rect.height:0 报错：需要检验是否存在
						h += data?Math.floor(data.height):0
						// h += Math.floor(data.height)
						item.bottom = h
					}).exec()
				})
			},
			pay() {
				//同步缓存
				//即购物车这个东西是不需要存到数据库的，但是又很多地方需要他
				//因此cart缓存到本地
				uni.setStorageSync('cart', this.cart)
				//这种跳转方式是可以返回的，因此返回的时候发现购物车没有消失
				uni.navigateTo({
					url: '/pages/pay/pay'
				})
			}
		}
	}
</script>

<!-- 注册样式可以写成.scss的格式分开成另一个文件，再用import进行引入即可 -->
<style lang="scss">
	@import './index.scss';
</style>
