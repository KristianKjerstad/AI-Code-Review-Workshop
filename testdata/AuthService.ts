// FILE: AuthService.ts

class AuthService {
    private token: string | null = null;
  
    login(username: string, password: string): boolean {
      if (username === 'admin' && password === 'admin') {
        this.token = 'mock-token-1234';
        return true;
      }
      return false;
    }
  
    logout(): void {
      this.token = null;
    }
  
    isAuthenticated(): boolean {
      return !!this.token;
    }
  
    getToken(): string {
      if (!this.token) {
        throw new Error('Not authenticated');
      }
      return this.token;
    }
  }
  
  export default new AuthService();
  