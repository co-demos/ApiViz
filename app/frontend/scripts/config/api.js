export const apiConfig = Object.freeze({

  // APIVIZ backend URL
  // rootURL: 'http://localhost:8100/backend/api',
  // rootURLpreprod: 'https://preprod.sonum-beta.fr/backend/api',
  // rootURLprod: 'http://sonum-beta.fr/backend/api',

  // toktokURL: 'http://localhost:4100/api',
  // toktokURLpreprod: 'https://preprod.toktok.sonum-beta.fr/backend/api',
  // toktokURLprod: 'http://toktok.sonum-beta.fr/backend/api',

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
    rootURL: 'http://sonum-beta.fr/backend/api',
    toktokURL: 'http://sonum-beta.fr/backend/api',
  }

})
