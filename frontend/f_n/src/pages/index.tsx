import Head from 'next/head'
import { useRouter } from 'next/router'
import Image from 'next/image'
import { useForm, SubmitHandler } from 'react-hook-form'
import { useState } from 'react'
import useAuth from '../hooks/useAuthnew'

import User from '../services/userService'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
// import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'

const inter = Inter({ subsets: ['latin'] })

interface Inputs {
  username: string
}



function Login() {
  const router = useRouter()
  const [login, setLogin] = useState(false)
  const { resetAuth } = useAuth()

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()

  let resp
  const { user } = useAuth()
  const onSubmit: SubmitHandler<Inputs> = async (data: any) => {
    if (login) {
       await resetAuth(data.username).then((r)=>r)
    }
  }

  return (
    <>
      <Head>
        <title>Personal Sourcing</title>
        <meta name="description" content="Personal Sourcing project" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main className={styles.main}>
        <div className={styles.description}>
          <p>
            Find your next software engineer...{user?.email}{resp}&nbsp;
            {/* <code className={styles.code}>src/pages/index.tsx</code> */}
          </p>
          <div>
            <a
              href="#"
              // target="_blank"
              rel="noopener noreferrer"
            >
              <Image
                src="/google.png "
                alt="Vercel Logo"
                className={styles.vercelLogo}
                width={50}
                height={10}
                priority
              />
            </a>
          </div>
        </div>

                    <div className={styles.center}>
                <div>
                <br></br>
                   <div className = "container">
                        <div className = "row">
                            <div className = "card col-md-6">
                                <h1 className='m-auto font-bold f-10'>
                                    Enter your email to reset password&nbsp;
                                    {/* <code className={styles.code}></code> */}
                                  </h1>



                                <div className = "card-body">
                                    <form
                                    onSubmit={handleSubmit(onSubmit)}
                                    >
                                        {/* --------------FORM START------------- */}
                                        <div className = "form-group">
                                            <input 
                                            placeholder="Email Address"
                                            type='email'
                                            id='mail'
                                            className={`form-input px-12 py-2 rounded ${
                                            errors.username && 'border-b-2 border-orange-500'
                                          }`}
                                          {...register('username', { required: true })}
                                            />
                                            {errors.username && (
                                              <p className="p-1 text-[13px] font-light  text-orange-500">
                                                Please enter a valid email.
                                              </p>
                                            )}
                                        </div>
                                        
                                        <div className = "form-group w-full py-2">
                                        <button 
                                        onClick={() => setLogin(true)} 
                                        type="submit"
                                        className="btn border border-rounded w-full" 
                                        >Continue
                                        </button>
                                        </div>
                                        <div className='form-group w-full '>
                                          <div
                                          className={styles.flink2}
                                          >
                                          <div className={styles.grid2}>
                                          <div><p className='m-auto font-bold'>I remember my password</p></div>
                                            <div>
                                              <button
                                              onClick={() => router.push('/register')} 
                                              type="submit"
                                              className='m-auto font-bold'
                                              >
                                              <p className='text-blue-500'>
                                                Sign in
                                                </p>
                                              </button>
                                              </div>
                                          </div>
                                          </div>
                                        </div>
                                        {/* --------------Forgot pass link------------- */}
                                        <div className='form-group w-full'>
                                          <div
                                          className={styles.flink2}
                                          >
                                          <div className={styles.grid2}>
                                          <div><p className='m-auto font-bold'>Don&lsquo;t have an account?</p></div>
                                            <div>
                                              <button
                                              onClick={() => router.push('/forgotpass')} 
                                              type="submit"
                                              className='m-auto font-bold'
                                              >
                                              <p className='text-blue-500'>
                                                Sign up
                                                </p>
                                              </button>
                                              </div>
                                          </div>
                                          </div>
                                        </div>
                                        {/* --------------FORM END------------- */}
                                    </form>
                                </div>
                            </div>
                        </div>

                   </div>
            </div>
        </div>

        <div className={styles.grid}>
          <a
            href="#"
            className={styles.card}
            // target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Categorising <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Ability to Categorise programming languages and&nbsp;respond.
            </p>
          </a>

          <a
            href="#"
            className={styles.card}
            // target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Learning <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Abilitiy to learn diffrent programming languages and &nbsp;learn on diffrent projects!
            </p>
          </a>

          <a
            href="#"
            className={styles.card}
            // target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Comparing <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Ability to compare diffrent projects and&nbsp;compile them accordingly and&nbsp;accurately.
            </p>
          </a>

          <a
            href="#"
            className={styles.card}
            // target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Grading <span>-&gt;</span>
            </h2>
            <p className={inter.className}>
              Ability to grade diffrent projects accurately and
              with&nbsp;remarks.
            </p>
          </a>
        </div>
      </main>
    </>
  )
}

export default Login
