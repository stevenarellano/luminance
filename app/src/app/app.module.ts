import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { PromptComponent } from './prompt/prompt.component';

import { CurriculumService } from './services/curriculum.service';
import { RoadmapComponent } from './roadmap/roadmap.component';
@NgModule({
  declarations: [AppComponent, LandingPageComponent, PromptComponent, RoadmapComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [CurriculumService],
  bootstrap: [AppComponent],
})
export class AppModule {}
