import { Component } from '@angular/core';
import { CurriculumService } from '../services';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss'],
})
export class LandingPageComponent {
  constructor(private curriculumService: CurriculumService) {}

  get curriculum() {
    return this.curriculumService.curriculum;
  }
}

export interface TopicPrompt {
  topic: string;
}
