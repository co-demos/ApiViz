export const apiConfig = Object.freeze({

  // APIVIZ backend URL
  // SWITCHES FOR DYNAMIC SETTING
  
  default : {
    rootURL: 'http://localhost:8100/backend/api',
  },

  preprod : {
    rootURL: 'https://preprod.sonum-beta.fr/backend/api',
  },

  production : {
    rootURL: 'https://sonum-beta.fr/backend/api',
  }

})
