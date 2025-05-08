import axios from 'axios';

// 定义基础 URL，根据实际情况修改
const baseURL = 'https://your-api-url.com'; // 这里替换为你的实际 API 地址

// 封装 POST 请求
const post = async (params: any = {}) => {
  const {
    url,
    data,
    config = {}
  } = params;

  try {
    const response = await axios.post(
      `${baseURL}${url}`,
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

export {
  post
};
