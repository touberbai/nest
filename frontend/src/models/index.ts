

/**
 * 将列表转化为Class
 * @param params
 * @param params.list 列表
 * @param params.module Class
 *
 * @returns {*[]|*}
 */
function listConvertToModel (params: any) {
  if (!params) {
    return []
  }
  const { list, model } = params ?? {}
  if (!list) {
    return []
  }
  if (list.length === 0) {
    return []
  }
  if (!model) {
    return list
  }
  const modelList: any[] = []
  list.forEach((item: any) => {
    const new_classes = new model(item)
    modelList.push(new_classes)
  })
  return modelList
}



/**
 * 更新模型
 * @param params
 */
const updateModel = (obj: any, model: any) => {
  if (!isObject(obj)) {
    return
  }
  if (!isObject(model)) {
    return
  }
  for (let key in model) {
    if (canInit(model[key])) {
      model[key] = (model[key] ?? '') !== '' ? model[key] : (obj && (obj[key] ?? '' !== "") ? obj[key] : '')
    } else {
      // eslint-disable-next-line no-self-assign
      model[key] = model[key]
    }
  }
}

function isObject (variable: any) {
  // 使用 typeof 判断变量是否为 'object'
  // 并且排除 null（因为 typeof null 也是 'object'）
  return variable !== null && typeof variable === 'object';
}

function canInit (value: any) {
  if (typeof value === 'function') {
    return false
  }
  return !(typeof value === 'object' && value !== null);
}

export {
  listConvertToModel,
  updateModel,
}
