import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from "@angular/router";
import { FormsModule } from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";

import { AppComponent } from './app.component';
import { HeaderComponent } from './containers/header/header.component';
import { ImageSideComponent } from './components/image-side/image-side.component';
import { HorizontalMenuComponent } from './components/horizontal-menu/horizontal-menu.component';
import { HomeComponent } from './containers/home/home.component';

const appRoutes: Routes = [
  {path: "", component: HomeComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    ImageSideComponent,
    HorizontalMenuComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes, {enableTracing: true}),
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
