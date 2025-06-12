
const BlogRouter = [
  {
    path: '/blog',
    name: 'Blog',
    component: () => import('@/layouts/blog.vue'),
    children: [
      {
        path: '',
        name: 'BlogIndex',
        component: () => import('@/views/blog/index.vue')
      },
      {
        path: 'editor',
        name: 'BlogEditor',
        component: () => import('@/views/blog/editor.vue'),
        meta: {
          hideNavigation: true,
        }
      },
    ]
  }
]

export default BlogRouter
