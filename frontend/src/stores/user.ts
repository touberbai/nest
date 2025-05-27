import { defineStore } from 'pinia';
import { ref, computed, watch } from 'vue';
import User from '@/models/modules/user';
// import { fetchUserInfo, login as apiLogin, logout as apiLogout } from '@/api/user';
// import { useToast } from 'vue-toastification';
// import router from '@/router';

export const useUserStore = defineStore('user', () => {
  // 状态管理
  const user = ref<User | null>(null);
  const loading = ref<boolean>(false);
  const error = ref<string | null>(null);

  // 从本地存储恢复用户状态
  const initUser = localStorage.getItem('user');
  if (initUser) {
    try {
      user.value = JSON.parse(initUser) as User;
    } catch (e) {
      console.error('Failed to parse user data from localStorage', e);
    }
  }

  // 监听用户状态变化，自动持久化到本地存储
  watch(user, (newUser) => {
    if (newUser) {
      localStorage.setItem('user', JSON.stringify(newUser));
    } else {
      localStorage.removeItem('user');
    }
  }, { deep: true });

  // 获取用户信息
  const fetchUser = async () => {
    // loading.value = true;
    // error.value = null;
    //
    // try {
    //   const response = await fetchUserInfo();
    //   user.value = response.data;
    //   return response.data;
    // } catch (err: any) {
    //   error.value = err.message || 'Failed to fetch user info';
    //   user.value = null;
    //   return null;
    // } finally {
    //   loading.value = false;
    // }
  };

  // 用户登录
  const login = async (email: string, password: string) => {
    loading.value = true;
    try {
      const res = await await User.login(email, password);
      console.log(res)
      user.value = new User(res)
      return true
    } catch (err: any) {
      return false
    } finally {
      loading.value = false
    }

    return res
  }
  // const login = async (credentials: { username: string; password: string }) => {
    // loading.value = true;
    // error.value = null;
    //
    // try {
    //   const response = await apiLogin(credentials);
    //   user.value = response.data;
    //   useToast().success('登录成功');
    //   await router.push('/dashboard');
    //   return true;
    // } catch (err: any) {
    //   error.value = err.response?.data?.message || '登录失败，请检查凭证';
    //   useToast().error(error.value);
    //   return false;
    // } finally {
    //   loading.value = false;
    // }
  // };

  // 用户登出
  const logout = async () => {
    // loading.value = true;
    // error.value = null;
    //
    // try {
    //   await apiLogout();
    //   user.value = null;
    //   useToast().success('已成功登出');
    //   await router.push('/login');
    //   return true;
    // } catch (err: any) {
    //   error.value = err.message || '登出失败';
    //   useToast().error(error.value);
    //   return false;
    // } finally {
    //   loading.value = false;
    // }
  };

  // 更新用户信息
  // const updateUser = async (userData: Partial<User>) => {
    // loading.value = true;
    // error.value = null;
    //
    // try {
    //   if (!user.value) throw new Error('User not logged in');
    //
    //   const response = await apiUpdateUser({
    //     ...user.value,
    //     ...userData
    //   });
    //
    //   user.value = response.data;
    //   useToast().success('用户信息已更新');
    //   return true;
    // } catch (err: any) {
    //   error.value = err.message || '更新用户信息失败';
    //   useToast().error(error.value);
    //   return false;
    // } finally {
    //   loading.value = false;
    // }
  // };

  // 清除错误信息
  const clearError = () => {
    error.value = null;
  };

  // 派生状态
  const isAuthenticated = computed(() => !!user.value);
  // const userRole = computed(() => user.value?.role || 'guest');
  // const userId = computed(() => user.value?.id || null);

  return {
    user,
    loading,
    error,
    isAuthenticated,
    // userRole,
    // userId,
    fetchUser,
    login,
    logout,
    // updateUser,
    clearError
  };
});
