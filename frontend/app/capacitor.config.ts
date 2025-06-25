import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'io.ionic.starter',
  appName: 'app',
  webDir: 'www',

  plugins: {
    SplashScreen: {
    launchShowDuration: 3000, // duración en milisegundos
    launchAutoHide: false, // no lo ocultes automáticamente
    backgroundColor: "#ffffff",
    showSpinner: true,
    spinnerColor: "#999999"
    },
  },
  


};


export default config;
