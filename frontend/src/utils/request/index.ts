import axios from 'axios';

// 定义基础 URL，根据实际情况修改
// const baseURL = import.meta.env.VITE_API_BASE_URL; // 这里替换为你的实际 API 地址

// 封装 POST 请求
const postJson = async (params: any = {}) => {
  const {
    url,
    data,
    config = {}
  } = params;

  try {
    const response = await axios.post(
      // `${baseURL}${url}`,
      url,
      data,
      {
        ...config,
        headers: {
          'Content-Type': 'application/json',
          ...config.headers
        }
      }
    );
    return response.data;
  } catch (error) {
    console.error('POST 请求错误:', error);
    throw error;
  }
};

// 封装 POST 请求，发送 form-data 格式的数据
const post = async (params: any = {}) => {
  const {
    url,
    data,
    config = {}
  } = params;

  const formData = new FormData();
  for (const key in data) {
    if (data.hasOwnProperty(key)) {
      formData.append(key, data[key]);
    }
  }

  try {
    const response = await axios.post(
      url,
      formData,
      {
        ...config,
        headers: {
          'Content-Type': 'multipart/form-data',
          ...config.headers
        }
      }
    );
    console.log(response)
    return response.data;
  } catch (error) {
    console.error('POST form-data 请求错误:', error);
    throw error;
  }
};


export {
  post,
  postJson
};
