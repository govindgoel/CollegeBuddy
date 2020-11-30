import React from 'react';
import Head from 'next/head';
import { string } from 'prop-types';

const content = "CollegeBuddy||By the students|Of the students|For the Students";

const Header = (props) => (
  <Head>
    <title>{props.title} | CollegeBuddy</title>
    <meta charSet="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta
      name="description"
      content={content}
    />
    <meta name="keywords" content={props.keywords} />
    <meta property="og:title" content={`${props.title} | amFOSS CMS`} />
    <meta property="og:image" content={props.ogImage} />
    <meta
      property="og:description"
      content={content}
    />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:url" content="https://my.amfoss.in" />
    <meta name="twitter:title" content="amFOSS CMS" />
    <meta
      name="twitter:description"
      content={content}
    />
    <meta
      name="twitter:image"
      content="https://avatars.githubusercontent.com/amfoss"
    />
    <meta name="twitter:creator" content="College_Buddy" />
    <meta name="theme-color" content="#ff6600" />
    <meta name="apple-mobile-web-app-title" content="College Buddy" />
    <meta name="apple-mobile-web-app-status-bar-style" content="default" />
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="mobile-web-app-capable" content="yes" />
    <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon" />
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    <link rel="apple-touch-icon" type="image/png" href="/static/favicon.ico" />
    <link rel="manifest" href="/static/manifest.json" />
  </Head>
);

Header.propTypes = {
  title: string,
  description: string,
  keywords: string,
  url: string,
  ogImage: string,
};

export default Header;
