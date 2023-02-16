import Head from 'next/head'
import Image from 'next/image'
import { useForm, SubmitHandler } from 'react-hook-form'
import { useState } from 'react'
import useAuth from '../hooks/useAuth'
import { Inter } from '@next/font/google'
import styles from '@/styles/Home.module.css'
// import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'

const inter = Inter({ subsets: ['latin'] })

interface Inputs {
  username: string
  password: string
  remember_password: boolean
}

function Home() {
  const [login, setLogin] = useState(false)
  // const { signIn, signUp } = useAuth()

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()

  const onSubmit: SubmitHandler<Inputs> = async (data: any) => {
    //console.log(data)
    if (login) {
      //console.log("data123")
      await useAuth.signIn(data.username, data.password)
    } else {
      //console.log("data456")
     await useAuth.signUp(data.username, data.password)
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
            Find your next software engineer...&nbsp;
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
                                    Welcome back&nbsp;
                                    {/* <code className={styles.code}></code> */}
                                  </h1>



                                <div className = "card-body">
                                    <form
                                    onSubmit={handleSubmit(onSubmit)}
                                    >
                                        {/* ---------------SOCIAL LINK START------------ */}
                                        
                                        <div className='form-group w-full'>
                                          <a
                                          href="#"
                                          className={styles.flink}
                                          rel="noopener noreferrer"
                                          >
                                          <div className={styles.grid2}>
                                            <div>
                                            <Image
                                              src="/github.png"
                                              alt="13"
                                              width={20}
                                              height={20}
                                              priority
                                            />
                                            </div>
                                            <div><p className='font-bold'>Continue with Github</p></div>
                                          </div>
                                          </a>
                                        </div>

                                        <div className='form-group w-full py-2'>
                                          <a
                                          href="#"
                                          className={styles.flink}
                                          rel="noopener noreferrer"
                                          >
                                          <div className={styles.grid2}>
                                            <div>
                                            <Image
                                              src="/google.png"
                                              alt="13"
                                              width={20}
                                              height={20}
                                              priority
                                            />
                                            </div>
                                            <div><p className='font-bold'>Continue with Google</p></div>
                                          </div>
                                          </a>
                                        </div>

                                        {/* <div className='form-group w-full'>
                                          <a
                                          href="#"
                                          className={styles.flink}
                                          rel="noopener noreferrer"
                                          >
                                          <div className={styles.grid2}>
                                            <div>
                                            <Image
                                              src="/linkedin.png"
                                              alt="13"
                                              width={17}
                                              height={17}
                                              priority
                                            />
                                            </div>
                                            <div><p className='font-bold'>Continue with Linkedin</p></div>
                                          </div>
                                          </a>
                                        </div> */}
                                        {/* ---------------SOCIAL LINK END------------ */}
                                        {/* ---------------OR LINE START------------ */}
                                        <div className='form-group w-full py-2'>
                                          <div
                                          className={styles.flink2}
                                          >
                                          <div className={styles.grid3}>
                                            <div className={styles.line}>
                                            </div>
                                            <div><p className='m-auto font-bold'>OR</p></div>
                                            <div className={styles.line}>
                                            </div>
                                          </div>
                                          </div>
                                        </div>
                                        {/* --------------OR LINE END------------- */}
                                        {/* --------------FORM START------------- */}
                                        <div className = "form-group">
                                            <input 
                                            placeholder="Email Address"
                                            type='email'
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
                                        <div className = "form-group py-2">
                                            <input 
                                            placeholder="Password"
                                            {...register('password', { required: true })}
                                            type='password'
                                            className={`form-input px-12 rounded ${
                                              errors.password && 'border-b-2 border-orange-500'
                                            }`}
                                            />
                                            {errors.password && (
                                              <p className="p-1 text-[13px] font-light  text-orange-500">
                                                Your password must contain between 4 and 60 characters.
                                              </p>
                                            )}
                                        </div>
                                        <div className = "form-group w-full">
                                        <button 
                                        onClick={() => setLogin(true)} 
                                        type="submit"
                                        className="btn border border-rounded w-full" 
                                        >Continue
                                        </button>
                                        </div>
                                        {/* --------------Remmember pass box------------- */}
                                        <div className='form-group w-full'>
                                          <div
                                          className={styles.flink2}
                                          >
                                          <div className={styles.grid2}>
                                          <div>
                                            <input 
                                            
                                            type="checkbox" 
                                            {...register('remember_password', { required: false })}
                                            id="" 
                                            className='form-checkbox rounded-full text-blue-500' 
                                            />
                                          </div>
                                          <div><p className='m-auto text-semi-bold'>Remember your password?</p></div>
                                          </div>
                                          </div>
                                        </div>
                                        {/* --------------Register Link------------- */}
                                        <div className='form-group w-full '>
                                          <div
                                          className={styles.flink2}
                                          >
                                          <div className={styles.grid2}>
                                          <div><p className='m-auto font-bold'>Don't have an account?</p></div>
                                            <div>
                                              <button
                                              onClick={() => setLogin(false)} 
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
                                        {/* --------------Forgot pass link------------- */}
                                        <div className='form-group w-full'>
                                          <div
                                          className={styles.flink2}
                                          >
                                          <div className={styles.grid2}>
                                          <div><p className='m-auto font-bold'>Forgot your password?</p></div>
                                            <div>
                                              <button
                                              onClick={() => setLogin(false)} 
                                              type="submit"
                                              className='m-auto font-bold'
                                              >
                                              <p className='text-blue-500'>
                                                Reset here
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

export default Home
