import { updateModel } from '@/models/index.ts'
import { post } from '@/utils/request'
/**
 * 博客文章
 */
class BlogPost {
  id: number | string = ''
  title: string = ''
  content: string = ''
  category_id: number | string = ''
  category: any
  comments: any
  likes: any

  constructor (params = {}) {
    this.updateData(params)
  }

  updateData (params = {}) {
    updateModel(params, this)
  }

  static async create (params: any = {}) {
    const blogPost = new BlogPost(params)
    return await blogPost.save()
  }

  async save () {
    const data = {
      title: this.title,
      content: this.content,
    }

    const res = await post({
      url: '/api/posts/create',
      data
    });
    this.updateData(res)
    return res
  }

}

export default BlogPost
