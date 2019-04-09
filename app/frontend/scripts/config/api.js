export const apiConfig = Object.freeze({

  // APIVIZ backend URL
  // SWITCHES FOR DYNAMIC SETTING
  
  default : {
    rootURL: 'http://localhost:8100/backend/api',
    // authURL: 'http://localhost:4100/api',
    // userURL: 'http://localhost:4100/api',
  },

  preprod : {
    rootURL: 'https://preprod.sonum-beta.fr/backend/api',
    // authURL: 'https://preprod.toktok.co-demos.com/api',
    // userURL: 'https://preprod.toktok.co-demos.com/api',
  },

  production : {
    rootURL: 'https://sonum-beta.fr/backend/api',
    // authURL: 'https://toktok.co-demos.com/api',
    // userURL: 'https://toktok.co-demos.com/api',
  }

})
