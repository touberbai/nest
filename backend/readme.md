### 启动命令(文档)

1. 启动后端服务
要确保你的后端服务正在运行。你可以通过以下命令启动后端服务（前提是你已经安装了所有依赖）：
```bash
  uvicorn main:app --reload --port 7778
```
这里假定你的主文件是 `backend/main.py`，并且端口号设置为 `7778`。
2. 访问 Swagger UI 文档
FastAPI 默认会为你的 API 生成 Swagger UI 文档。当你的后端服务启动后，在浏览器中访问以下 URL：
plaintext
`http://127.0.0.1:7778/docs`
你会看到一个交互式的 API 文档界面，其中包含了所有定义的 API 端点，以及每个端点的详细信息，如请求方法、请求参数、响应格式等。你还可以在这个界面直接测试 API 接口，输入请求参数并发送请求，查看响应结果。
3. 访问 ReDoc 文档
除了 Swagger UI，FastAPI 还支持 ReDoc 文档。在浏览器中访问以下 URL 来查看 ReDoc 文档：
plaintext
`http://127.0.0.1:7778/redoc`
ReDoc 提供了一个简洁、美观的 API 文档界面，同样包含了所有 API 端点的详细信息，但风格与 Swagger UI 有所不同。
4. 文档中的 API 端点信息
在文档中，你可以找到每个 API 端点的详细信息，包括：
请求方法：如 GET、POST 等。
请求路径：API 的具体路径。
请求参数：包括路径参数、查询参数、请求体参数等。
响应格式：API 返回的响应数据格式。
5. 测试 API 接口
在 Swagger UI 文档中，你可以直接测试 API 接口。找到你想要测试的 API 端点，点击 Try it out 按钮，输入请求参数，然后点击 Execute 按钮发送请求。你可以在下方看到请求的详细信息和响应结果。

## web列表

- vue3
- vite
- pinia
- element-plus
- axios
- vue-router
- mockjs
- scss
- tiptap 富文本编辑器

## python 列表
- fastapi