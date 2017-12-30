import { Injectable } from "@angular/core";
import { Apollo } from "apollo-angular";
import gql from "graphql-tag";
import { CategoryModel } from "../models/category.model";

import "rxjs/add/operator/toPromise";

@Injectable()
export class CategoryService {
  constructor(private apollo: Apollo) { }

  getAllCategories() {
    let allCategoriesQuery = gql`{
      allCategories {
        name, description
      }
    }`;

    this.apollo.query({query: allCategoriesQuery})
      .toPromise()
      .then(console.log);

  }

}
