import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "path"


// https://vitejs.dev/config/
export default defineConfig({
  
  server: {
    port:3000,
    watch: {
        usePolling: true
    }
},
  plugins: [react()],
  build: {
    outDir: 'dist'
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})


