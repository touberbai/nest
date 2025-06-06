import {
  updateModel,
} from '@/models'


class Token {
  access_token: string = ''
  refresh_token: string = ''

  constructor (params: any ) {
    this.updateData(params)
  }

  updateData(params: any = {}) {
    updateModel(params, this)
  }
}


export default Token
