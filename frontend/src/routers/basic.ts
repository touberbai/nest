import OptionRouter from '@/routers/modules/option.ts'
const BasicRouter = [
  {
    path: '/',
    component: () => import('@/layouts/basic.vue'),
    children: [
      ...OptionRouter,
    ]
  }
]

export default BasicRouter
