export const apiConfig = Object.freeze({

  // APIVIZ backend URL
  // SWITCHES FOR DYNAMIC SETTING
  
  default : {
    rootURL: 'http://localhost:8100/backend/api',
    toktokURL: 'http://localhost:4100/api',
  },

  preprod : {
    rootURL: 'https://preprod.sonum-beta.fr/backend/api',
    toktokURL: 'https://preprod.toktok.sonum-beta.fr/backend/api',
  },

  production : {
    rootURL: 'https://sonum-beta.fr/backend/api',
    toktokURL: 'https://sonum-beta.fr/backend/api',
  }

})
