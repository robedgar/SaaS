import type { NextPage } from 'next';
import Head from 'next/head';
import Image from 'next/image';
import styles from '@/styles/Home.module.css';
import CopyKitt from '@/components/copyKitt';

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>CopyKitt | AI Generated Marketing</title>
        <meta
          name="description"
          content="Generate branding snippets for your products"
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <CopyKitt />
    </div>
  );
};

export default Home;
