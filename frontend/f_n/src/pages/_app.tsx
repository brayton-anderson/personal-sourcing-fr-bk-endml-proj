import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import Head from 'next/head';
import { Toaster } from 'react-hot-toast'
import { RecoilRoot } from 'recoil'
import { AuthProvider } from '../hooks/useAuthnew'
//import { Nav, Alert } from '../components/Alert'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
    <RecoilRoot>
    <AuthProvider>
    <Toaster position="top-center" />
    <Component {...pageProps} />
    </AuthProvider>
    </RecoilRoot>
    
    </>
  );
}

//<Component {...pageProps} />