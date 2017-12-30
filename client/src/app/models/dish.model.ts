import { CategoryModel} from "./category.model";

export class DishModel {
  name: String;
  category: CategoryModel;
  description: String;
  price: Number;
}
