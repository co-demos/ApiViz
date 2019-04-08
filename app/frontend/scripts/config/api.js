export const apiConfig = Object.freeze({

  // APIVIZ backend URL
  // SWITCHES FOR DYNAMIC SETTING
  
  default : {
    rootURL: 'http://localhost:8100/backend/api',
    authURL: 'http://localhost:4100/api/auth',
    userURL: 'http://localhost:4100/api/usr',
  },

  preprod : {
    rootURL: 'https://preprod.sonum-beta.fr/backend/api',
    authURL: 'https://preprod.toktok.sonum-beta.fr/api/auth',
    userURL: 'http://preprod.toktok.sonum-beta.fr/api/usr',
  },

  production : {
    rootURL: 'https://sonum-beta.fr/backend/api',
    authURL: 'https://toktok.sonum-beta.fr/api/auth',
    userURL: 'http://toktok.sonum-beta.fr/api/usr',
  }

})
