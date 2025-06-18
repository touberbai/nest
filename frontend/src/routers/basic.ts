import FutureRouter from '@/routers/modules/future.ts'
import OptionRouter from '@/routers/modules/option.ts'
const BasicRouter = [
  {
    path: '/',
    component: () => import('@/layouts/basic.vue'),
    children: [
      ...FutureRouter,
      ...OptionRouter,
    ]
  }
]

export default BasicRouter
