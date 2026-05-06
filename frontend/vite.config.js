import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],

  // Force Vite to realize it's the center of the universe
  root: process.cwd(),
  
  server: {
    // Explicitly set the HMR port to avoid conflicts with your FastAPI backend
    hmr: {
      protocol: 'ws',
      host: 'localhost',
    },
    watch: {
      usePolling: true,
      interval: 100, // Check every 100ms
    },
  },
})

