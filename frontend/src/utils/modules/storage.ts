// nest/frontend/src/utils/storage.ts
const storage = {
  // 保存数据到本地存储
  setLocalStorage(key: string, value: any) {
    try {
      const serializedValue = JSON.stringify(value);
      localStorage.setItem(key, serializedValue);
    } catch (error) {
      console.error('Error saving to localStorage:', error);
    }
  },
  // 从本地存储获取数据
  getLocalStorage(key: string) {
    try {
      const serializedValue = localStorage.getItem(key);
      if (serializedValue === null) {
        return null;
      }
      return JSON.parse(serializedValue);
    } catch (error) {
      console.error('Error getting from localStorage:', error);
      return null;
    }
  },
  // 从本地存储删除数据
  removeLocalStorage(key: string) {
    try {
      localStorage.removeItem(key);
    } catch (error) {
      console.error('Error removing from localStorage:', error);
    }
  },
  // 保存数据到会话存储
  setSessionStorage(key: string, value: any) {
    try {
      const serializedValue = JSON.stringify(value);
      sessionStorage.setItem(key, serializedValue);
    } catch (error) {
      console.error('Error saving to sessionStorage:', error);
    }
  },
  // 从会话存储获取数据
  getSessionStorage(key: string) {
    try {
      const serializedValue = sessionStorage.getItem(key);
      if (serializedValue === null) {
        return null;
      }
      return JSON.parse(serializedValue);
    } catch (error) {
      console.error('Error getting from sessionStorage:', error);
      return null;
    }
  },
  // 从会话存储删除数据
  removeSessionStorage(key: string) {
    try {
      sessionStorage.removeItem(key);
    } catch (error) {
      console.error('Error removing from sessionStorage:', error);
    }
  },
};

export default storage;
