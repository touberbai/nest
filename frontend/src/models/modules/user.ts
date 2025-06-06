import {
  updateModel,
} from '@/models'
// import md5 from 'md5'
import { post } from '@/utils/request'

class User {
  id: number = 0
  username: string = ''
  // password
  email: string = ''
  verification_code?: number
  code_expiration_time?: number
  is_active?: number
  access_token?: string
  refresh_token?: string

  constructor (params: any = {} ) {
    this.updateData(params)
  }

  updateData(params: any = {}) {
    updateModel(params, this)
  }

  static regist = async (email: string, password: string) => {
    const res = await post({
      url: '/api/register',
      data: {
        email,
        password
      }
    });
    return res;
  }


  static login = async (email: string, password: string) => {
    const res = await post({
      url: '/api/login',
      data: {
        email,
        password
      }
    })
    return res
  }

  logout = async () => {

  }


}


export default User
