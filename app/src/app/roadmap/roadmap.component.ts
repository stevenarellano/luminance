import { Component } from '@angular/core';
import { CurriculumService } from '../services';

@Component({
  selector: 'app-roadmap',
  templateUrl: './roadmap.component.html',
  styleUrls: ['./roadmap.component.scss'],
})
export class RoadmapComponent {
  constructor(private curriculumService: CurriculumService) {}

  get curriculum() {
    return this.curriculumService.curriculum;
  }
}
