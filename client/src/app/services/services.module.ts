import { NgModule } from '@angular/core';

import { HttpClientModule } from "@angular/common/http"
import { ApolloModule, Apollo } from "apollo-angular";
import { HttpLinkModule, HttpLink } from "apollo-angular-link-http";

import { CategoryService } from "./category.service";
import { DishService} from "./dish.service";
import {InMemoryCache} from "apollo-cache-inmemory";

import { XSRFStrategy, CookieXSRFStrategy} from "@angular/http"; // Deprecated in favor of using
// "@angular/common/http" but it doesn't work: https://angular.io/api/http/CookieXSRFStrategy

@NgModule({
  declarations: [
  ],
  imports: [
    HttpClientModule,
    ApolloModule,
    HttpLinkModule
  ],
  providers: [
    { provide: XSRFStrategy, useValue: new CookieXSRFStrategy('csrftoken', 'X-CSRFToken') },
    CategoryService,
    DishService
  ]
})
export class ServicesModule {
  constructor(private apollo: Apollo, private httpLink: HttpLink) {
    apollo.create({
      link: httpLink.create({ uri: 'http://localhost:8000/graphql/'}),
      cache: new InMemoryCache()
    });
  }
}
