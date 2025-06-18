const FutureRouter = [
  {
    path: 'future',
    name: 'Future', // 路由名称
    component: () => import('@/views/future/index.vue'),
  },
  // 收益计算
//   {
//     path: 'option_profit_calculation',
//     name: 'OptionProfitCalculation',
//     component: () => import('@/views/option/profit_calculation.vue'),
//   }
]

export default FutureRouter
