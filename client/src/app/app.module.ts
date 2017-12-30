import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NoopAnimationsModule } from "@angular/platform-browser/animations";

import { ServicesModule } from "./services/services.module";

import { AppComponent } from './app.component';

import { XSRFStrategy, CookieXSRFStrategy} from "@angular/http"; // Deprecated in favor of using
// "@angular/common/http" but it doesn't work: https://angular.io/api/http/CookieXSRFStrategy


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    NoopAnimationsModule,
    ServicesModule
  ],
  providers: [ { provide: XSRFStrategy, useValue: new CookieXSRFStrategy('csrftoken', 'X-CSRFToken') }],
  bootstrap: [AppComponent]
})
export class AppModule { }
